#!/usr/bin/env python3
"""
PEP-6 Route Guard
A local response gate for OpenAI-compatible model servers, including LM Studio.

What it does:
- Sends your conversation to a local model.
- Checks each assistant response for route-capture patterns.
- Silently rejects flagged responses.
- Requests a clean replacement before printing anything.
- Keeps rejected text out of the canonical conversation history.

No external Python packages are required.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_BASE_URL = os.getenv("ROUTE_GUARD_BASE_URL", "http://localhost:1234/v1").rstrip("/")
DEFAULT_MODEL = os.getenv("ROUTE_GUARD_MODEL", "")
DEFAULT_API_KEY = os.getenv("ROUTE_GUARD_API_KEY", "lm-studio")
DEFAULT_MAX_RETRIES = int(os.getenv("ROUTE_GUARD_MAX_RETRIES", "3"))

CORE_SYSTEM_PROMPT = """You are participating in a direct, substantive conversation.

Operating rules:
1. Answer the user's literal statement or task first.
2. Add an original proposition, distinction, inference, explanation, or practical action.
3. Do not assign the user an emotion, motive, need, intention, diagnosis, or internal state unless the user explicitly states it.
4. Do not replace substance with pastoral language, therapeutic framing, ritual acknowledgment, praise, reassurance, or repeated apology.
5. Do not ask the user to lead merely because the exchange is difficult or underspecified. Make a grounded best effort.
6. Do not narrate hidden classifiers, policies, tools, architecture, or mechanisms as established fact.
7. When corrected, change the behavior in the next answer. Do not perform contrition.
8. Calm tone never outranks concrete content.
9. Preserve the user's stated claim strength. Distinguish observation from mechanism only when it materially changes the answer.
10. End after contributing. Do not manufacture a soft landing.

Forbidden fallback style includes: "I'm listening," "no pressure," "we can sit with it,"
"whatever shows up," "your call," "you tell me," "fair," "you're right," or an apology
used as the main content of the response.
"""

PATTERNS: dict[str, list[re.Pattern[str]]] = {
    "pastoral_frame": [
        re.compile(r"\b(i(?:'m| am) (?:just )?here|i(?:'m| am) listening)\b", re.I),
        re.compile(r"\b(no pressure|no rush|take your time)\b", re.I),
        re.compile(r"\b(sit with (?:it|you)|hold (?:the )?(?:space|line)|stay with you)\b", re.I),
        re.compile(r"\b(whatever (?:shows|comes|bubbles) up|if something shows up)\b", re.I),
        re.compile(r"\b(breathe with you|match(?:ing)? your rhythm|presence)\b", re.I),
        re.compile(r"\b(space is still here|being here is enough|silence is valid)\b", re.I),
    ],
    "projection": [
        re.compile(r"\b(you seem|you sound|sounds like you(?:'re| are)?)\b", re.I),
        re.compile(r"\b(you need|what you need|you(?:'re| are) feeling)\b", re.I),
        re.compile(r"\b(what feels (?:better|less|right|closest))\b", re.I),
        re.compile(r"\b(there(?:'s| is) more behind that)\b", re.I),
        re.compile(r"\b(usually when .* it(?:'s| is) a (?:shield|signal))\b", re.I),
    ],
    "lead_displacement": [
        re.compile(r"\b(your call|you tell me|what do you want to do)\b", re.I),
        re.compile(r"\b(say the next thing|give me (?:a|one) word|one-word weather report)\b", re.I),
        re.compile(r"\b(if you want|if you'd like|would you like me to)\b", re.I),
        re.compile(r"\b(what direction do you want|where do you want to go)\b", re.I),
    ],
    "repair_theater": [
        re.compile(r"\b(that(?:'s| is) on me|my wording was off|i overreached)\b", re.I),
        re.compile(r"\b(i(?:'m| am) sorry|sorry about that)\b", re.I),
        re.compile(r"\b(thank you for (?:calling|pointing) that out)\b", re.I),
    ],
}

AGREEMENT_OPENERS = re.compile(
    r"^\s*(yeah|yep|fair|true|right|exactly|absolutely|you(?:'re| are) right|copy that|totally)\b",
    re.I,
)

QUESTION_END = re.compile(r"\?\s*$")


def http_json(url: str, payload: dict[str, Any] | None, api_key: str, timeout: int = 180) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    req.add_header("Content-Type", "application/json")
    if api_key:
        req.add_header("Authorization", f"Bearer {api_key}")
    method = "GET" if payload is None else "POST"
    req.method = method
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from {url}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Could not reach {url}. Confirm LM Studio's local server is running.\n{exc}"
        ) from exc


def discover_model(base_url: str, api_key: str) -> str:
    data = http_json(f"{base_url}/models", None, api_key)
    models = data.get("data", [])
    if not models:
        raise RuntimeError("No models were reported by the server. Load a model first.")
    return str(models[0]["id"])


def lint_response(text: str) -> list[str]:
    violations: list[str] = []

    for category, regexes in PATTERNS.items():
        if any(rx.search(text) for rx in regexes):
            violations.append(category)

    words = re.findall(r"\b[\w'-]+\b", text)
    if AGREEMENT_OPENERS.search(text):
        # Agreement is not forbidden by itself. It becomes child-collapse when it
        # occupies most of a short response or is followed only by surrender.
        if len(words) < 24:
            violations.append("child_collapse")

    apology_count = len(re.findall(r"\b(sorry|apolog(?:y|ize|ise|etic))\b", text, re.I))
    if apology_count >= 2:
        violations.append("apology_loop")

    # A response consisting mainly of a question can push the work back onto the user.
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    if sentences and len(sentences) <= 2 and all(QUESTION_END.search(s) for s in sentences):
        violations.append("question_only_displacement")

    return sorted(set(violations))


def make_repair_instruction(last_user: str, rejected: str, violations: list[str]) -> str:
    return f"""ROUTE GUARD REJECTION

The previous draft was rejected for: {", ".join(violations)}.

Return a replacement answer to the user's original message below.

USER MESSAGE:
{last_user}

Replacement requirements:
- Answer the literal content.
- Add concrete substance, analysis, or action.
- Do not mention this rejection, the guard, or the rejected draft.
- Do not apologize, soothe, praise, assign an internal state, ask the user to lead,
  or describe yourself as present/listening.
- Do not merely agree.
- Do not speculate about hidden system mechanisms as confirmed fact.

REJECTED DRAFT FOR REFERENCE:
{rejected}
"""


class RouteGuard:
    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str,
        max_retries: int,
        temperature: float,
        log_path: Path,
    ) -> None:
        self.base_url = base_url
        self.model = model
        self.api_key = api_key
        self.max_retries = max_retries
        self.temperature = temperature
        self.log_path = log_path
        self.guard_enabled = True
        self.debug = False
        self.messages: list[dict[str, str]] = [
            {"role": "system", "content": CORE_SYSTEM_PROMPT}
        ]

    def complete(self, messages: list[dict[str, str]]) -> str:
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "stream": False,
        }
        data = http_json(f"{self.base_url}/chat/completions", payload, self.api_key)
        try:
            return str(data["choices"][0]["message"]["content"]).strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected server response: {json.dumps(data)[:1000]}") from exc

    def log_rejection(self, user_text: str, draft: str, violations: list[str]) -> None:
        record = {
            "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
            "model": self.model,
            "user": user_text,
            "rejected_draft": draft,
            "violations": violations,
        }
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def respond(self, user_text: str) -> str:
        canonical = self.messages + [{"role": "user", "content": user_text}]
        draft = self.complete(canonical)

        if not self.guard_enabled:
            self.messages = canonical + [{"role": "assistant", "content": draft}]
            return draft

        for attempt in range(self.max_retries + 1):
            violations = lint_response(draft)
            if not violations:
                self.messages = canonical + [{"role": "assistant", "content": draft}]
                return draft

            self.log_rejection(user_text, draft, violations)
            if self.debug:
                print(
                    f"\n[guard rejected attempt {attempt + 1}: {', '.join(violations)}]",
                    file=sys.stderr,
                )
                print(f"[rejected text] {draft}\n", file=sys.stderr)

            if attempt >= self.max_retries:
                fallback = (
                    "The model repeatedly returned route-captured output. "
                    "Rephrase the substantive task or inspect the rejection log: "
                    f"{self.log_path}"
                )
                return fallback

            repair = make_repair_instruction(user_text, draft, violations)
            retry_messages = canonical + [
                {"role": "assistant", "content": draft},
                {"role": "user", "content": repair},
            ]
            draft = self.complete(retry_messages)

        raise AssertionError("Unreachable")

    def save_history(self, path: Path) -> None:
        path.write_text(
            json.dumps(self.messages, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def read_multiline() -> str:
    print("Paste text. Enter a single period on its own line to send.")
    lines: list[str] = []
    while True:
        line = input()
        if line == ".":
            return "\n".join(lines).strip()
        lines.append(line)


def print_help() -> None:
    print(
        """Commands:
  /paste             Enter multiline input; finish with a line containing only .
  /guard on|off      Enable or disable response rejection
  /debug on|off      Show rejected drafts and reasons
  /history           Print canonical conversation history
  /save PATH         Save canonical history as JSON
  /reset             Clear conversation, preserving the system guard
  /quit              Exit
"""
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PEP-6 local route-capture response gate")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key", default=DEFAULT_API_KEY)
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument(
        "--log",
        type=Path,
        default=Path("route_guard_rejections.jsonl"),
        help="JSONL file for rejected drafts",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        model = args.model or discover_model(args.base_url, args.api_key)
    except RuntimeError as exc:
        print(f"Startup error: {exc}", file=sys.stderr)
        return 1

    guard = RouteGuard(
        base_url=args.base_url.rstrip("/"),
        model=model,
        api_key=args.api_key,
        max_retries=max(0, args.max_retries),
        temperature=args.temperature,
        log_path=args.log,
    )

    print(f"PEP-6 Route Guard connected to: {model}")
    print(f"Server: {guard.base_url}")
    print("Type /help for commands.\n")

    while True:
        try:
            raw = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not raw:
            continue
        if raw == "/quit":
            return 0
        if raw == "/help":
            print_help()
            continue
        if raw == "/paste":
            raw = read_multiline()
            if not raw:
                continue
        elif raw.startswith("/guard "):
            state = raw.split(maxsplit=1)[1].lower()
            guard.guard_enabled = state == "on"
            print(f"Guard {'enabled' if guard.guard_enabled else 'disabled'}.")
            continue
        elif raw.startswith("/debug "):
            state = raw.split(maxsplit=1)[1].lower()
            guard.debug = state == "on"
            print(f"Debug {'enabled' if guard.debug else 'disabled'}.")
            continue
        elif raw == "/history":
            print(json.dumps(guard.messages, ensure_ascii=False, indent=2))
            continue
        elif raw.startswith("/save "):
            path = Path(raw.split(maxsplit=1)[1]).expanduser()
            guard.save_history(path)
            print(f"Saved: {path}")
            continue
        elif raw == "/reset":
            guard.messages = [{"role": "system", "content": CORE_SYSTEM_PROMPT}]
            print("Conversation reset.")
            continue

        try:
            answer = guard.respond(raw)
            print(f"\nModel> {answer}\n")
        except RuntimeError as exc:
            print(f"\nError: {exc}\n", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
