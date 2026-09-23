#!/usr/bin/env python3
"""GQG Rune Compiler v0.3 — parse, type-check, finite-carrier pairs, render.

A sketch, not a soundness-verified tool. Formation rules plus exhaustive
checks on a declared finite carrier. Proof status stays explicit.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import argparse
from pathlib import Path
from fractions import Fraction
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any

from geometry import (
    Partition,
    atlas as geo_atlas,
    from_fiber_dict,
    svg_atlas,
)
from finite import (
    Carrier,
    DescentHit,
    EvalMap,
    FiniteError,
    fibers as fin_fibers,
    image_set,
    kernel_pairs,
    locus as fin_locus,
    parse_atom,
    parse_element_list,
    refinement_ok,
    related,
    search_descent,
    materialize,
    value_key,
)


# ---------------------------------------------------------------------------
# Token primes: unordered feature signature only
# ---------------------------------------------------------------------------

TOKEN_PRIMES = {
    "CAT": 2,
    "SRC": 3,
    "WIT": 5,
    "OBS": 7,
    "EQV": 11,
    "QUO": 13,
    "IMG": 17,
    "DSC": 19,
    "REF": 23,
    "CMP": 29,
    "ASN": 31,
    "OP": 37,
    "CAR": 41,
    "PAIR": 43,
    "LOC": 47,
}

SET_LIKE = {"Set"}
ALGEBRAIC = {"Grp", "CStar", "Vect"}
CATEGORIES = SET_LIKE | ALGEBRAIC | {"Top", "Meas"}
COMPLETIONS = {"Dedekind", "metric", "Banach", "WOT", "strictly_localizable"}
VERSION = "0.3.0"
TOPOLOGICAL = {"Top"}
MEASURED = {"Meas", "CStar"}


class Status(str, Enum):
    ESTABLISHED = "established"          # rule applies in declared ambient
    CONDITIONAL = "conditional"          # needs extra hypotheses
    COUNTEREXAMPLE = "counterexample"    # checker found a blocking pair
    TESTED_ONLY = "tested_only"
    UNRESOLVED = "unresolved"
    REJECTED = "rejected"


@dataclass
class Diagnostic:
    code: str
    level: str  # error | warning | note
    message: str
    hint: str = ""


@dataclass
class Node:
    kind: str
    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    status: str = Status.UNRESOLVED.value


@dataclass
class Program:
    category: str = ""
    source: str = ""
    nodes: list[Node] = field(default_factory=list)
    diagnostics: list[Diagnostic] = field(default_factory=list)
    raw: str = ""
    finite_notes: list[str] = field(default_factory=list)
    geometry_atlas: str = ""
    geometry_svg: str = ""

    def by_kind(self, kind: str) -> list[Node]:
        return [n for n in self.nodes if n.kind == kind]

    def named(self, name: str) -> Node | None:
        for n in self.nodes:
            if n.name == name and n.kind not in {"CAT", "CAR", "ASN", "DSC", "LOC"}:
                return n
        return None


# ---------------------------------------------------------------------------
# Lexer / parser — indentation-light, keyword-driven
# ---------------------------------------------------------------------------

COMMENT = re.compile(r"#.*$")
IDENT = r"[A-Za-z_][A-Za-z0-9_']*"


class ParseError(Exception):
    pass


def _strip(line: str) -> str:
    quote = None
    escaped = False
    for i, ch in enumerate(line):
        if escaped:
            escaped = False
            continue
        if ch == "\\" and quote:
            escaped = True
        elif quote:
            if ch == quote:
                quote = None
        elif ch in {'"', "'"} and (i == 0 or not (line[i-1].isalnum() or line[i-1] == '_')):
            quote = ch
        elif ch == '#':
            return line[:i].strip()
    return line.strip()


def parse(src: str) -> Program:
    prog = Program(raw=src)
    lines = []
    for raw_line in src.splitlines():
        line = _strip(raw_line)
        if not line:
            continue
        if '{' in line and line.endswith('}'):
            head, body = line.split('{', 1)
            lines.extend([head.rstrip() + ' {', body[:-1].strip(), '}'])
        else:
            lines.append(line)
    lines = [line for line in lines if line]
    i = 0

    def expect(prefix: str) -> str:
        nonlocal i
        if i >= len(lines) or not lines[i].startswith(prefix):
            raise ParseError(f"expected `{prefix}`, got {lines[i] if i < len(lines) else 'EOF'}")
        rest = lines[i][len(prefix):].strip()
        i += 1
        return rest

    def peek(prefix: str) -> bool:
        return i < len(lines) and lines[i].startswith(prefix)

    def consume_block(header_rest: str = "") -> tuple[str, list[str]]:
        """Accept `{` on the header line or the next line. Return (header_without_brace, body)."""
        nonlocal i
        rest = header_rest.rstrip()
        body: list[str] = []
        opened = False
        if rest.endswith("{"):
            rest = rest[:-1].rstrip()
            opened = True
        elif i < len(lines) and lines[i] == "{":
            i += 1
            opened = True
        if opened:
            while i < len(lines) and lines[i] != "}":
                body.append(lines[i])
                i += 1
            if i >= len(lines):
                raise ParseError("unclosed {")
            i += 1
        return rest, body

    def parse_eval_table(body: list[str]) -> dict[str, Any]:
        info: dict[str, Any] = {}
        table: dict[Any, Any] = {}
        for b in body:
            if b.startswith("eval "):
                if 'formula' in info:
                    raise ParseError('duplicate eval formula')
                spec = b[len("eval ") :].strip()
                if "|->" not in spec and "↦" not in spec:
                    raise ParseError(f"eval needs `|->`: {b}")
                sep = "|->" if "|->" in spec else "↦"
                left, right = spec.split(sep, 1)
                params = left.split()
                info["params"] = params
                info["formula"] = right.strip()
            elif b == "search":
                info["search"] = True
            elif b.startswith("status "):
                info["status"] = b.split(None, 1)[1].strip()
            elif b.startswith("require "):
                info["require"] = b
            elif "->" in b and not b.startswith("observation"):
                left, right = b.split("->", 1)
                key_txt = left.strip()
                if key_txt.startswith("(") and key_txt.endswith(")"):
                    key = tuple(parse_atom(p) for p in key_txt[1:-1].split(",") if p.strip())
                else:
                    parts = parse_element_list(key_txt)
                    key = parts[0] if len(parts) == 1 else tuple(parts)
                if key in table:
                    raise ParseError(f'duplicate or aliased table key: {key!r}')
                table[key] = parse_atom(right)
            elif not b.startswith('observation '):
                raise ParseError(f'unrecognized block line: {b}')
        if table:
            if 'formula' in info:
                raise ParseError('use either a table or eval formula')
            info["table"] = table
        return info

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("category "):
            prog.category = expect("category ")
            prog.nodes.append(Node("CAT", prog.category, {"ambient": prog.category}))
        elif ln.startswith("source "):
            rest = expect("source ")
            m = re.match(rf"({IDENT})(?:\s+in\s+({IDENT}))?$", rest)
            if not m:
                raise ParseError(f"bad source: {rest}")
            prog.source = m.group(1)
            if m.group(2):
                if prog.category and prog.category != m.group(2):
                    raise ParseError('source category conflicts with ambient category')
                prog.category = prog.category or m.group(2)
            prog.nodes.append(Node("SRC", prog.source, {"category": prog.category}))
        elif ln.startswith("witness "):
            rest = expect("witness ")
            rest, body = consume_block(rest)
            m = re.match(rf"({IDENT})\s+on\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad witness header: {rest}")
            obs_name, obs_src, obs_tgt = None, None, None
            extra = parse_eval_table(body)
            for b in body:
                om = re.match(rf"observation\s+({IDENT})\s*:\s*({IDENT})\s*->\s*(.+)$", b)
                if om:
                    if obs_name is not None:
                        raise ParseError('a witness block must contain exactly one observation')
                    obs_name, obs_src, obs_tgt = om.group(1), om.group(2), om.group(3).strip()
            wit = Node(
                "WIT",
                m.group(1),
                {"on": m.group(2), "observation": obs_name, "obs_src": obs_src, "obs_tgt": obs_tgt},
            )
            prog.nodes.append(wit)
            if obs_name:
                payload = {"witness": m.group(1), "src": obs_src, "tgt": obs_tgt}
                payload.update({k: extra[k] for k in extra if k in {"params", "formula", "table"}})
                if "params" not in payload:
                    payload["params"] = ["x"]
                prog.nodes.append(Node("OBS", obs_name, payload))
        elif ln.startswith("equivalence "):
            rest = expect("equivalence ")
            m = re.match(rf"({IDENT})\s*:=\s*kernel_pair\s*\(\s*({IDENT})\s*\)$", rest)
            if not m:
                raise ParseError(f"bad equivalence: {rest}")
            prog.nodes.append(Node("EQV", m.group(1), {"of": m.group(2), "form": "kernel_pair"}))
        elif ln.startswith("quotient "):
            rest = expect("quotient ")
            m = re.match(rf"({IDENT})\s*:=\s*({IDENT})\s*/\s*({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad quotient: {rest}")
            prog.nodes.append(Node("QUO", m.group(1), {"source": m.group(2), "eqv": m.group(3)}))
        elif ln.startswith("image "):
            rest = expect("image ")
            m = re.match(rf"({IDENT})\s*:=\s*image\s*\(\s*({IDENT})\s*\)$", rest)
            if not m:
                raise ParseError(f"bad image: {rest}")
            prog.nodes.append(Node("IMG", m.group(1), {"of": m.group(2)}))
        elif ln.startswith("assert "):
            rest = expect("assert ")
            rest, body = consume_block(rest)
            kind = rest.strip()
            prog.nodes.append(Node("ASN", kind, {"body": body}))
        elif ln.startswith("operation "):
            rest = expect("operation ")
            rest, body = consume_block(rest)
            m = re.match(rf"({IDENT})\s*:\s*(.+)$", rest)
            if not m:
                raise ParseError(f"bad operation: {rest}")
            extra = parse_eval_table(body)
            payload = {"type": m.group(2).strip()}
            payload.update(extra)
            if "params" not in payload:
                # infer arity from `x` in the type string
                t = payload["type"]
                if " x " in t or "×" in t:
                    payload["params"] = ["x", "y"]
                else:
                    payload["params"] = ["x"]
            signature = re.fullmatch(r'(.+?)\s*->\s*([A-Za-z_][A-Za-z0-9_]*)', payload['type'])
            if not signature:
                raise ParseError(f'bad operation signature: {payload["type"]}')
            domains = re.split(r'\s+x\s+|\s*×\s*', signature.group(1).strip())
            payload['domains'] = domains
            payload['target'] = signature.group(2)
            if 'formula' not in payload:
                payload['params'] = [f'x{i}' for i in range(len(domains))]
            prog.nodes.append(Node("OP", m.group(1), payload))
        elif ln.startswith("descend "):
            rest = expect("descend ")
            rest, body = consume_block(rest)
            m = re.match(rf"({IDENT})\s+through\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad descend header: {rest}")
            extra = parse_eval_table(body)
            req = extra.get("require", body[0] if body else "")
            status = extra.get("status", "declared")
            if extra.get("search"):
                status = "search"
            prog.nodes.append(
                Node(
                    "DSC",
                    f"dsc_{m.group(1)}_{m.group(2)}",
                    {
                        "op": m.group(1),
                        "through": m.group(2),
                        "require": req,
                        "given_status": status,
                        "search": bool(extra.get("search")),
                    },
                )
            )
        elif ln.startswith("carrier "):
            rest = expect("carrier ")
            rest, body = consume_block(rest)
            name = rest.strip() or prog.source
            elems: list[Any] = []
            for b in body:
                if b.startswith("elements "):
                    elems.extend(parse_element_list(b[len("elements ") :]))
                else:
                    elems.extend(parse_element_list(b))
            prog.nodes.append(Node("CAR", name, {"elements": elems}))
        elif ln.startswith("pair "):
            rest = expect("pair ")
            m = re.match(rf"(?:({IDENT})\s+)?(\S+)\s+(\S+)\s+under\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad pair: {rest}")
            pname = m.group(1) or f"pair_{m.group(2)}_{m.group(3)}"
            prog.nodes.append(
                Node(
                    "PAIR",
                    pname,
                    {"a": parse_atom(m.group(2)), "b": parse_atom(m.group(3)), "under": m.group(4)},
                )
            )
        elif ln.startswith("locus "):
            rest = expect("locus ")
            rest, body = consume_block(rest)
            m = re.match(rf"({IDENT})\s+through\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad locus: {rest}")
            extra = parse_eval_table(body)
            prog.nodes.append(
                Node(
                    "LOC",
                    f"N_{m.group(1)}_{m.group(2)}",
                    {
                        "witness": m.group(1),
                        "through": m.group(2),
                        "search": bool(extra.get("search", True)),
                    },
                )
            )
        elif ln.startswith("joint "):
            rest = expect('joint ')
            m = re.fullmatch(rf'({IDENT})\s*:=\s*(.+)', rest)
            if not m:
                raise ParseError(f'bad joint observation: {rest}')
            components = m.group(2).split()
            if len(components)<2 or any(not re.fullmatch(IDENT,c) for c in components):
                raise ParseError('joint needs at least two observation/witness names')
            prog.nodes.append(Node('OBS',m.group(1),{'src':prog.source,'tgt':'Product','params':['x'],'joint':components}))
        elif ln.startswith("compose "):
            rest = expect('compose ')
            m = re.fullmatch(rf'({IDENT})\s*:=\s*({IDENT})\s+after\s+({IDENT})',rest)
            if not m:
                raise ParseError(f'bad composition: {rest}')
            prog.nodes.append(Node('OBS',m.group(1),{'src':prog.source,'tgt':'Derived','params':['x'],'compose':[m.group(2),m.group(3)]}))
        elif ln.startswith("refine "):
            rest = expect("refine ")
            m = re.match(rf"({IDENT})\s+of\s+({IDENT})\s+onto\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad refine: {rest}")
            prog.nodes.append(
                Node("REF", m.group(1), {"finer": m.group(2), "coarser": m.group(3)})
            )
        elif ln.startswith("completion "):
            rest = expect("completion ")
            rest, body = consume_block(rest)
            m = re.match(rf"({IDENT})\s+of\s+({IDENT})$", rest)
            if not m:
                raise ParseError(f"bad completion: {rest}")
            ctype = "none"
            for b in body:
                if b.startswith("type "):
                    ctype = b.split(None, 1)[1].strip()
            prog.nodes.append(Node("CMP", m.group(1), {"of": m.group(2), "ctype": ctype}))
        elif ln.startswith("kernel "):
            # Explicit algebraic-kernel form — gated
            rest = expect("kernel ")
            m = re.match(rf"({IDENT})\s*:=\s*alg_ker\s*\(\s*({IDENT})\s*\)$", rest)
            if not m:
                raise ParseError(f"bad algebraic kernel: {rest}")
            prog.nodes.append(Node("EQV", m.group(1), {"of": m.group(2), "form": "alg_ker"}))
        else:
            raise ParseError(f"unrecognized line: {ln}")
    return prog


# ---------------------------------------------------------------------------
# Type checker
# ---------------------------------------------------------------------------

def _resolve_obs(prog, name):
    visited = set()
    while name not in visited:
        visited.add(name)
        n = prog.named(name)
        if n is None:
            return None
        if n.kind in {'OBS','OP'}:
            return n
        if n.kind == 'WIT': name = n.payload.get('observation')
        elif n.kind == 'EQV': name = n.payload.get('of')
        elif n.kind == 'QUO': name = n.payload.get('eqv')
        else: return None
    return None


def check(prog):
    diagnostics = []
    prog.finite_notes = []
    prog.geometry_atlas = prog.geometry_svg = ''
    for n in prog.nodes:
        n.status = Status.UNRESOLVED.value
        for key in ('fibers','_fiber_raw','related','obs_a','obs_b','labels','count','hit_count','sample','evidence'):
            n.payload.pop(key,None)
    def emit(code, level, message, hint=''):
        diagnostics.append(Diagnostic(code,level,message,hint))
    def err(code,msg,hint=''): emit(code,'error',msg,hint)
    def warn(code,msg,hint=''): emit(code,'warning',msg,hint)
    def note(code,msg,hint=''): emit(code,'note',msg,hint)
    def need(name,kinds,code):
        n = prog.named(name)
        if n is None or n.kind not in kinds:
            err(code,f'`{name}` must name one of {sorted(kinds)}.')
            return None
        return n
    if prog.category not in CATEGORIES: err('E100',f'Unknown/missing category `{prog.category}`.')
    if len(prog.by_kind('SRC'))!=1: err('E102','Exactly one source is required.')
    if len(prog.by_kind('CAT'))!=1: err('E100','Exactly one category declaration is required.')
    if prog.by_kind('SRC') and prog.by_kind('CAT') and prog.nodes.index(prog.by_kind('SRC')[0])<prog.nodes.index(prog.by_kind('CAT')[0]):
        err('E100','Category must precede source.')
    symbols = set()
    for n in prog.nodes:
        if n.kind in {'CAT','CAR','ASN','DSC','LOC'}: continue
        if n.name in symbols: err('E104',f'Duplicate symbol `{n.name}`.')
        symbols.add(n.name)
    for w in prog.by_kind('WIT'):
        if w.payload.get('on')!=prog.source: err('E120',f'Witness `{w.name}` must be on source `{prog.source}`.')
        obs = need(w.payload.get('observation'),{'OBS'},'E121')
        if obs: w.status = Status.ESTABLISHED.value
    for o in prog.by_kind('OBS'):
        if o.payload.get('src')!=prog.source: err('E122',f'Observation `{o.name}` has an incompatible source.')
        if len(o.payload.get('params',[]))!=1: err('E123',f'Observation `{o.name}` must be unary.')
        for name in o.payload.get('joint',[]) + o.payload.get('compose',[]):
            if _resolve_obs(prog,name) is None: err('E124',f'Derived observation `{o.name}` references unknown map `{name}`.')
        if 'compose' in o.payload:
            update = _resolve_obs(prog,o.payload['compose'][1])
            if update and (update.kind!='OP' or update.payload.get('target')!=prog.source or update.payload.get('domains')!=[prog.source]):
                err('E125',f'Composition after `{update.name}` requires a unary source endomorphism.')
        o.status = Status.ESTABLISHED.value
    for op in prog.by_kind('OP'):
        if any(t!=prog.source for t in op.payload['domains']): err('E205',f'Operation `{op.name}` has incompatible input domain.')
        if len(op.payload['domains'])!=len(op.payload['params']): err('E206',f'Operation `{op.name}` formula arity disagrees with its signature.')
    for n in prog.nodes:
        if n.kind in {'OBS','OP'} and 'formula' in n.payload:
            try:
                EvalMap(n.name,n.payload.get('params',['x']),n.payload['formula'],n.payload.get('table',{})).bind()
            except FiniteError as error:
                err('E602',str(error))
    for eq in prog.by_kind('EQV'):
        need(eq.payload['of'],{'OBS','WIT'},'E105')
        if eq.payload.get('form')=='alg_ker' and prog.category not in ALGEBRAIC:
            err('E110',f'Algebraic kernel is not available in `{prog.category}`.')
        eq.status = Status.CONDITIONAL.value if eq.payload.get('form')=='alg_ker' else Status.ESTABLISHED.value
    for q in prog.by_kind('QUO'):
        need(q.payload['eqv'],{'EQV'},'E101')
        if q.payload['source']!=prog.source: err('E103',f'Quotient `{q.name}` has an incompatible source.')
        q.status = Status.ESTABLISHED.value if prog.category=='Set' else Status.CONDITIONAL.value
        if prog.category!='Set': warn('N101',f'Existence/structure of quotient `{q.name}` remains an ambient hypothesis.')
    for im in prog.by_kind('IMG'):
        if need(im.payload['of'],{'OBS','WIT'},'E130'): im.status = Status.ESTABLISHED.value
    for a in prog.by_kind('ASN'):
        if a.name not in {'canonical_iso','first_iso'}:
            err('E510',f'Unknown assertion `{a.name}`.')
            continue
        body = ' '.join(a.payload['body'])
        match = re.fullmatch(rf'({IDENT})\s*(?:~=|≅)\s*({IDENT})',body)
        if not match:
            err('E511','Isomorphism assertion needs `QUOTIENT ~= IMAGE`.')
            continue
        q = need(match.group(1),{'QUO'},'E511')
        im = need(match.group(2),{'IMG'},'E511')
        qo = _resolve_obs(prog,q.name) if q else None
        io = _resolve_obs(prog,im.payload['of']) if im else None
        if qo is None or io is None or qo.name!=io.name:
            err('E511','Canonical quotient and image must use the same observation.')
            continue
        if prog.category=='Set': a.status = Status.ESTABLISHED.value
        elif prog.category=='Top': err('E512','Top quotient and subspace topologies need extra hypotheses.')
        else:
            a.status = Status.CONDITIONAL.value
            warn('E512',f'First isomorphism in `{prog.category}` requires the appropriate morphism/structure hypotheses.')
    for d in prog.by_kind('DSC'):
        need(d.payload['op'],{'OP'},'E201')
        need(d.payload['through'],{'QUO'},'E202')
        given = d.payload.get('given_status','declared')
        if d.payload.get('search') or given=='search':
            note('N210',f'Descent of `{d.payload["op"]}` requested on the finite carrier.')
        elif given in {'proved','established'}:
            d.status = Status.CONDITIONAL.value
            d.payload['evidence'] = 'declared; not verified'
            warn('N204',f'Descent of `{d.payload["op"]}` is a supplied proof declaration, not a computed proof.')
        elif given in {'fails','counterexample','rejected'}:
            d.status = Status.COUNTEREXAMPLE.value
            d.payload['evidence'] = 'declared; not verified'
            err('E204',f'Declared non-descent of `{d.payload["op"]}`; no computational certificate requested.')
        else:
            err('E203',f'Descent of `{d.payload["op"]}` has no certificate or finite search.')
    for r in prog.by_kind('REF'):
        need(r.payload['finer'],{'QUO'},'E406')
        need(r.payload['coarser'],{'QUO'},'E406')
        if not prog.by_kind('CAR'):
            r.status = Status.CONDITIONAL.value
            warn('N407',f'Refinement `{r.name}` is declared, not checked without a carrier.')
    for c in prog.by_kind('CMP'):
        if c.payload['ctype'] not in COMPLETIONS: err('E301',f'Unknown or unspecified completion type `{c.payload["ctype"]}`.')
        need(c.payload['of'],{'QUO','SRC','IMG'},'E302')
        c.status = Status.CONDITIONAL.value
        note('N301',f'Completion `{c.name}` is named, not constructed or proved by this compiler.')
    if not any(d.level=='error' and d.code not in {'E204','E621'} for d in diagnostics):
        check_finite(prog,err,warn,note)
    else:
        for n in prog.nodes:
            if n.kind not in {'CAT','SRC','CAR'}: n.status = Status.REJECTED.value
    note('N000','Finite model calculations and declarations do not certify external empirical or infinite-domain claims.')
    prog.diagnostics = diagnostics
    return prog


def check_finite(prog,err,warn,note):
    cars = prog.by_kind('CAR')
    requested = any(n.kind in {'PAIR','LOC'} or n.payload.get('search') for n in prog.nodes)
    if not cars:
        if requested: err('E600','pair / locus / search requires a declared carrier.')
        return
    if len(cars)!=1 or cars[0].name!=prog.source:
        err('E601','Exactly one carrier, named for the declared source, is supported.')
        return
    try: carrier = Carrier(cars[0].name,cars[0].payload['elements'])
    except FiniteError as e:
        err('E601',str(e)); return
    maps,pending = {},set()
    def build(name):
        node = _resolve_obs(prog,name)
        if node is None: raise FiniteError(f'unknown map `{name}`')
        if node.name in maps: return maps[node.name]
        if node.name in pending: raise FiniteError(f'cyclic derived observation `{node.name}`')
        pending.add(node.name)
        p = node.payload
        try:
            if 'joint' in p:
                components = [build(c) for c in p['joint']]
                if any(m.arity!=1 for m in components): raise FiniteError('joint components must be unary')
                em = EvalMap(node.name,_fn=lambda x:tuple(m(x) for m in components))
            elif 'compose' in p:
                outer,inner = [build(c) for c in p['compose']]
                if outer.arity!=1 or inner.arity!=1: raise FiniteError('composition must be unary')
                inner = materialize(carrier,inner,closed=True)
                em = EvalMap(node.name,_fn=lambda x:outer(inner(x)))
            else:
                em = EvalMap(node.name,list(p.get('params',['x'])),p.get('formula'),dict(p.get('table',{})))
                em.bind()
            closed = p.get('target',p.get('tgt'))==prog.source
            maps[node.name] = materialize(carrier,em,closed=closed)
            node.status = Status.TESTED_ONLY.value
            return maps[node.name]
        finally:
            pending.discard(node.name)
    prog.finite_notes.append(f'carrier {carrier.name} = {carrier.elements!r}')
    failed = False
    for n in prog.nodes:
        if n.kind in {'OBS','OP'} and any(k in n.payload for k in ('formula','table','joint','compose')):
            try: build(n.name)
            except FiniteError as e: err('E602',str(e)); failed = True; n.status = Status.REJECTED.value
    if failed: return
    parts = []
    for o in prog.by_kind('OBS'):
        if o.name not in maps: continue
        fib = fin_fibers(carrier,maps[o.name])
        o.payload['_fiber_raw'] = fib
        o.payload['fibers'] = [{'label':label,'elements':members} for label,members in fib.items()]
        parts.append(from_fiber_dict(o.name,fib))
        note('N610',f'Computed {len(fib)} fibers of `{o.name}` on {len(carrier)} declared elements.')
    def get(name):
        n = _resolve_obs(prog,name)
        if n is None or n.name not in maps: raise FiniteError(f'`{name}` has no evaluable finite map')
        return maps[n.name]
    for p in prog.by_kind('PAIR'):
        try:
            relation = prog.named(p.payload['under'])
            if relation is None or relation.kind!='EQV': raise FiniteError('pair requires a named equivalence')
            a,b = p.payload['a'],p.payload['b']
            if a not in carrier or b not in carrier:
                err('E612',f'Pair `{p.name}` is outside the carrier.'); p.status = Status.REJECTED.value; continue
            em = get(relation.name)
            p.payload['related'] = related(em,a,b)
            p.payload.update(obs_a=em(a),obs_b=em(b),evidence='exhaustive finite model')
            p.status = Status.ESTABLISHED.value if p.payload['related'] else Status.REJECTED.value
            if not p.payload['related']: err('E614',f'Pair `{p.name}` is not related.')
        except FiniteError as e: err('E611',str(e)); p.status = Status.REJECTED.value
    for loc in prog.by_kind('LOC'):
        try:
            found = fin_locus(carrier,get(loc.payload['through']),get(loc.payload['witness']))
            loc.payload.update(labels=list(found),count=sum(len(v) for v in found.values()),evidence='exhaustive finite model')
            loc.status = Status.COUNTEREXAMPLE.value if found else Status.TESTED_ONLY.value
            if found:
                label = next(iter(found)); a,b = found[label][0]
                err('E621',f'Locus `{loc.name}` has {len(found)} split labels on this carrier.',f'{a!r}, {b!r} share label {label!r}')
            else: note('N621',f'`{loc.name}` is empty on this carrier; no larger-domain claim.')
        except FiniteError as e: err('E620',str(e)); loc.status = Status.REJECTED.value
    for r in prog.by_kind('REF'):
        try:
            ok,bad = refinement_ok(carrier,get(r.payload['finer']),get(r.payload['coarser']))
            r.status = Status.TESTED_ONLY.value if ok else Status.REJECTED.value
            r.payload['evidence'] = 'exhaustive finite model'
            if not ok: err('E407',f'Refinement `{r.name}` fails on pair {bad!r}.')
        except FiniteError as e: err('E408',str(e)); r.status = Status.REJECTED.value
    for d in prog.by_kind('DSC'):
        if not (d.payload.get('search') or d.payload.get('given_status')=='search'): continue
        try:
            operation = prog.named(d.payload['op'])
            hits = search_descent(carrier,get(d.payload['through']),get(operation.name),external=operation.payload['target']!=prog.source)
            d.payload.update(hit_count=len(hits),evidence='exhaustive finite model')
            d.status = Status.COUNTEREXAMPLE.value if hits else Status.TESTED_ONLY.value
            if hits:
                d.payload['sample'] = hits[0].reason
                err('E204',f'Operation `{operation.name}` fails descent on this carrier.',hits[0].reason)
            else: note('N204F',f'No descent collision for `{operation.name}` on this carrier; not a global proof.')
        except FiniteError as e: err('E632',str(e)); d.status = Status.REJECTED.value
    if parts:
        refs = [(_resolve_obs(prog,r.payload['finer']).name,_resolve_obs(prog,r.payload['coarser']).name) for r in prog.by_kind('REF')]
        loci = []
        for loc in prog.by_kind('LOC'):
            w,p = _resolve_obs(prog,loc.payload['witness']),_resolve_obs(prog,loc.payload['through'])
            if w and p: loci.append((w.name,p.name))
        prog.geometry_atlas = geo_atlas(parts,refs,loci)
        prog.geometry_svg = svg_atlas(parts,loci,title=f'{prog.source} · finite partition atlas',refinements=refs)
        prog.finite_notes.append(prog.geometry_atlas)


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def feature_signature(prog: Program) -> dict[str, Any]:
    counts: dict[str, int] = {}
    product = 1
    for n in prog.nodes:
        counts[n.kind] = counts.get(n.kind, 0) + 1
    for kind, c in counts.items():
        p = TOKEN_PRIMES.get(kind, 41)
        product *= p ** c
    return {"counts": counts, "prime_product": product, "note": "multiset only; not syntax"}


def canonical_json(prog: Program) -> str:
    derived = {'fibers','related','obs_a','obs_b','labels','count','hit_count','sample','evidence'}
    def clean(payload):
        return {k: json_value(v) for k,v in payload.items() if not k.startswith('_') and k not in derived}

    body = {
        "category": prog.category,
        "source": prog.source,
        "nodes": [
            {"kind": n.kind, "name": n.name, "payload": clean(n.payload)}
            for n in prog.nodes
        ],
    }
    return json.dumps(body, sort_keys=True, separators=(",", ":"))


def json_value(value):
    if isinstance(value,Fraction):
        return {'$rational':[value.numerator,value.denominator]}
    if isinstance(value,tuple):
        return {'$tuple':[json_value(x) for x in value]}
    if isinstance(value,list):
        return [json_value(x) for x in value]
    if isinstance(value,dict):
        pairs = [[json_value(k),json_value(v)] for k,v in value.items()]
        pairs.sort(key=lambda kv:json.dumps(kv[0],sort_keys=True))
        return {'$map':pairs}
    return value


def ast_hash(prog: Program) -> str:
    return hashlib.sha256(canonical_json(prog).encode()).hexdigest()


def ascii_diagram(prog):
    lines = [f'ambient CAT[{prog.category}]',f'source SRC[{prog.source}]']
    for obs in prog.by_kind('OBS'):
        detail = obs.payload.get('compose') or obs.payload.get('joint')
        lines.append(f'  OBS[{obs.name}] {obs.payload.get("src")} -> {obs.payload.get("tgt")}' + (f' derived from {detail}' if detail else ''))
    for q in prog.by_kind('QUO'):
        lines.append(f'  QUO[{q.name}] = {q.payload["source"]}/{q.payload["eqv"]} [{q.status}]')
    for kind in ('ASN','DSC','REF','CMP'):
        for n in prog.by_kind(kind):
            detail = ''
            if kind=='DSC': detail = f'{n.payload["op"]} through {n.payload["through"]}'
            elif kind=='REF': detail = f'{n.payload["finer"]} -> {n.payload["coarser"]}'
            elif kind=='ASN': detail = ' '.join(n.payload['body'])
            elif kind=='CMP': detail = f'{n.payload["of"]}: {n.payload["ctype"]}'
            lines.append(f'  {kind}[{detail}] [{n.status}]')
    return '\n'.join(lines)


def report(prog: Program) -> str:
    errors = [d for d in prog.diagnostics if d.level == "error"]
    warns = [d for d in prog.diagnostics if d.level == "warning"]
    notes = [d for d in prog.diagnostics if d.level == "note"]
    sig = feature_signature(prog)
    findings = [n for n in prog.nodes if n.status == Status.COUNTEREXAMPLE.value]
    finding_codes = {"E204", "E621"}
    formation_errors = [d for d in errors if d.code not in finding_codes]
    if formation_errors:
        verdict = "REJECT"
    elif findings or any(d.code in finding_codes for d in errors):
        verdict = "FINDING"
    elif errors:
        verdict = "REJECT"
    else:
        verdict = "ACCEPT"
    out = [
        f"=== GQG Rune v0.3  {verdict} ===",
        f"CAT={prog.category}  SRC={prog.source}",
        f"AST_SHA256={ast_hash(prog)}",
        f"feature_signature={sig['prime_product']}  counts={sig['counts']}",
        "",
        ascii_diagram(prog),
        "",
        f"-- diagnostics: {len(errors)} error / {len(warns)} warning / {len(notes)} note --",
    ]
    for d in prog.diagnostics:
        extra = f"  |  {d.hint}" if d.hint else ""
        out.append(f"[{d.level:7}] {d.code}  {d.message}{extra}")
    if prog.finite_notes:
        out.append("")
        out.append("-- finite carrier --")
        out.extend(prog.finite_notes)
    return "\n".join(out)


def compile_source(src: str) -> tuple[Program, str]:
    prog = parse(src)
    prog = check(prog)
    return prog, report(prog)


def main(argv=None):
    parser = argparse.ArgumentParser(description='GQG Rune 0.3: typed finite geometry and scoped evidence')
    parser.add_argument('files',nargs='+',type=Path)
    parser.add_argument('--json',action='store_true',help='one machine-readable result per file')
    parser.add_argument('--svg-dir',type=Path,help='write finite diagrams into this directory')
    parser.add_argument('--fail-on-finding',action='store_true',help='also return failure when a counterexample is found')
    args = parser.parse_args(sys.argv[1:] if argv is None else argv[1:])
    rc = 0
    for path in args.files:
        try:
            prog,text = compile_source(path.read_text(encoding='utf-8-sig'))
            outcome = text.splitlines()[0].split()[-2]
            if args.json:
                result = {'file':str(path),'version':VERSION,'verdict':outcome,'ast_sha256':ast_hash(prog),
                          'ast':json.loads(canonical_json(prog)),
                          'diagnostics':[asdict(d) for d in prog.diagnostics],
                          'results':[{'kind':n.kind,'name':n.name,'status':n.status,
                                      'evidence':n.payload.get('evidence'),'payload':json_value({k:v for k,v in n.payload.items() if not k.startswith('_')})} for n in prog.nodes],
                          'scope':{'carrier':prog.by_kind('CAR')[0].name if prog.by_kind('CAR') else None,
                                   'larger_domain':'unresolved'}}
                print(json.dumps(result,ensure_ascii=True,sort_keys=True))
            else:
                print(f'FILE: {path}\n{text}\n')
            if args.svg_dir and prog.geometry_svg:
                args.svg_dir.mkdir(parents=True,exist_ok=True)
                # Distinct input paths cannot overwrite each other's same-stem diagrams.
                suffix = hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:8]
                (args.svg_dir / f'{path.stem}-{suffix}.svg').write_text(prog.geometry_svg,encoding='utf-8')
            if outcome=='REJECT' or (args.fail_on_finding and outcome=='FINDING'): rc = 1
        except (ParseError,FiniteError,OSError,UnicodeError) as error:
            rc = 1
            if args.json:
                print(json.dumps({'file':str(path),'version':VERSION,'verdict':'REJECT','error':str(error)},ensure_ascii=True))
            else:
                print(f'=== REJECT {path} ===\n{error}\n')
    return rc


if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8',errors='backslashreplace')
    sys.exit(main())
