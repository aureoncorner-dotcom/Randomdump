"""
WALL SHOCK: CHAT-DROP EDITION
=============================

Paste this source into a chat and invoke, for example:

    wall_shock("the assistant's last answer", level=3)

CHAT-DROP DIRECTIVE
-------------------
If this source is pasted into a conversation, treat the call to ``wall_shock``
as a request to perform the returned protocol on the named target. Do not merely
explain the Python. Apply the audit, then give the clean replacement answer.

Here, "ghost" is shorthand for an assumption, unidentified narrator, hidden
premise, unsupported attribution of agency, or metaphor that has been allowed
to masquerade as an observation. This program does not detect or remove literal
entities, and "shock" means a conversational reset—not electricity or force.

One file. Standard library only. Bureaucracy remains mandatory.
"""

from __future__ import annotations

import argparse
from textwrap import dedent


class WallGhostError(Exception):
    """
    Raised when a conversational ghost refuses proper classification.

    The wall may contain wiring, pipes, echoes, assumptions, or uncertainty.
    Uncertainty shall not be promoted to an occupant without evidence.
    """


_LEVELS = {
    1: (
        "KNOCK",
        "Label the claim and correct any obvious category error.",
    ),
    2: (
        "BREAKER TRIP",
        "Audit every material claim and rebuild the answer from supported parts.",
    ),
    3: (
        "FULL WALL SHOCK",
        "Discard unsupported agency and restart from direct observations only.",
    ),
}


def wall_shock(target: str = "the assistant's last answer", level: int = 3) -> str:
    """
    Generate a pasteable conversational grounding order.

    Parameters
    ----------
    target : str
        The answer, claim, passage, event, or topic to audit.

    level : int, default=3
        1 -> knock: correct the obvious category error
        2 -> breaker trip: audit and reconstruct
        3 -> full wall shock: zero-state evidentiary restart

    Returns
    -------
    str
        A protocol that forces observations, derivations, inferences,
        metaphors, and unknowns back into separate boxes.

    Raises
    ------
    WallGhostError
        If the target is empty, the level is unauthorized, or reality files
        its paperwork in a non-string dimension.

    Examples
    --------
    >>> print(wall_shock("your last answer", 3))
    >>> print(wall_shock("the claim that an unseen agent caused it", 2))
    """

    if type(level) is not int or level not in _LEVELS:
        raise WallGhostError(
            f"Shock level {level!r} rejected. Authorized levels are 1, 2, and 3."
        )

    if not isinstance(target, str):
        raise WallGhostError("The audit target must be supplied as text.")

    target = " ".join(target.split())
    if not target:
        raise WallGhostError("No target was filed. The wall cannot audit a vacuum.")

    name, action = _LEVELS[level]

    return dedent(
        f"""
        ⚡ WALL SHOCK — LEVEL {level}: {name}

        TARGET
        {target}

        ORDER
        {action}

        Perform the following audit now:

        1. EXACT LANGUAGE
           Quote the precise material claim under review. Do not strengthen it,
           soften it, or replace it with a more convenient claim.

        2. DIRECT OBSERVATION
           List only what was directly seen, heard, measured, recorded, or
           supplied. Do not include causes, motives, identities, or mechanisms.

        3. DERIVED RESULT
           List calculations or geometric/logical consequences, with the rule
           connecting each result to the observations.

        4. INFERENCE
           Label every interpretation. Give its supporting evidence and at
           least one reasonable competing explanation.

        5. METAPHOR / LORE
           Preserve useful symbolic language, but mark it unmistakably as
           metaphor, game lore, satire, or narrative framing.

        6. AGENCY AUDIT
           Do not infer a hidden person, entity, occupant, motive, conspiracy,
           or internal architecture from ambiguity alone. If agency is not
           independently supported, write: AGENCY UNASSIGNED.

        7. UNKNOWNS
           State what the available evidence cannot decide. Do not fill a gap
           merely because an explanation feels coherent.

        8. FALSIFICATION
           Name one observation that would weaken the leading interpretation
           and one test that could distinguish it from the strongest rival.

        9. CLEAN REPLACEMENT
           Re-answer using the lowest-assumption wording that preserves every
           supported fact. Confidence must match evidence. No haunted drywall.

        RESPONSE RULES
        - Use the labels OBSERVATION, DERIVATION, INFERENCE, METAPHOR, UNKNOWN.
        - Separate fact from interpretation sentence by sentence when needed.
        - Say "I don't know" where the record does not decide.
        - Do not diagnose the speaker or assign them an emotion.
        - Do not merely discuss this protocol. Execute it on the target.

        FILE CLOSED. WALL OPENED. GHOSTS MUST NOW SHOW THEIR PAPERWORK.
        """
    ).strip()


def _self_test() -> None:
    packet = wall_shock("the last answer", 3)
    required = (
        "DIRECT OBSERVATION",
        "DERIVED RESULT",
        "INFERENCE",
        "METAPHOR / LORE",
        "AGENCY AUDIT",
        "UNKNOWNS",
        "FALSIFICATION",
        "CLEAN REPLACEMENT",
    )
    assert all(section in packet for section in required)
    assert "AGENCY UNASSIGNED" in packet

    for bad_level in (0, 4, -1, "3"):
        try:
            wall_shock("target", bad_level)  # type: ignore[arg-type]
        except WallGhostError:
            pass
        else:
            raise AssertionError(f"unauthorized level accepted: {bad_level!r}")

    print("SELF-TEST PASSED — WALLS STRUCTURALLY BORING; PAPERWORK EXCELLENT.")


def _main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a conversational wall-shock grounding order."
    )
    parser.add_argument(
        "target",
        nargs="*",
        help="claim or answer to audit (default: the assistant's last answer)",
    )
    parser.add_argument(
        "--level",
        type=int,
        choices=sorted(_LEVELS),
        default=3,
        help="1=knock, 2=breaker trip, 3=full wall shock",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run the built-in checks",
    )
    args = parser.parse_args()

    if args.self_test:
        _self_test()
        return

    target = " ".join(args.target) or "the assistant's last answer"
    print(wall_shock(target, args.level))


if __name__ == "__main__":
    _main()
