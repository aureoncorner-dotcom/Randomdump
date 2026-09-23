"""Partition geometry for a finite carrier.

The picture is the partition, the refinement map, and the split fibers
of N_W(π). No shape is claimed beyond the discrete set of the carrier.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from typing import Any
import textwrap
from finite import FiniteError, value_key


def _lab(x: Any) -> str:
    if isinstance(x,tuple):
        return '(' + ', '.join(_lab(v) for v in x) + ')'
    return str(x)


def _cell(members: list[Any], width: int | None = None) -> str:
    body = " ".join(_lab(m) for m in members)
    inner = f" {body} "
    if width:
        inner = inner.center(width)
    return "[" + inner + "]"


@dataclass
class Partition:
    name: str
    fibers: dict[Any, list[Any]]  # label -> members, stable order

    def __post_init__(self):
        seen = set()
        for label,members in self.fibers.items():
            value_key(label)
            if not members:
                raise FiniteError('partition classes must be nonempty')
            for member in members:
                key = value_key(member)
                if key in seen:
                    raise FiniteError('each carrier element must occur in exactly one partition class')
                seen.add(key)

    @property
    def labels(self) -> list[Any]:
        return list(self.fibers.keys())

    def class_of(self, x: Any) -> Any:
        for lab, mem in self.fibers.items():
            if x in mem:
                return lab
        raise KeyError(x)

    def width_hint(self) -> int:
        if not self.fibers:
            return 3
        return max(len(" ".join(_lab(m) for m in mem)) + 2 for mem in self.fibers.values())


def from_fiber_dict(name: str, raw: dict[Any, list[Any]]) -> Partition:
    return Partition(name=name, fibers=dict(raw))


def compare(fine: Partition, coarse: Partition) -> str:
    """finer / coarser / equal / incomparable — set-level on the same carrier."""
    if {value_key(x) for members in fine.fibers.values() for x in members} != {value_key(x) for members in coarse.fibers.values() for x in members}:
        raise FiniteError('partition comparison requires the same carrier')
    fine_pairs = _pairs(fine)
    coarse_pairs = _pairs(coarse)
    f_in_c = fine_pairs <= coarse_pairs
    c_in_f = coarse_pairs <= fine_pairs
    if f_in_c and c_in_f:
        return "equal"
    if f_in_c:
        return "finer"  # fine equivalence is finer, so Q_fine ↠ Q_coarse
    if c_in_f:
        return "coarser"
    return "incomparable"


def _pairs(p: Partition) -> set[tuple[Any, Any]]:
    out: set[tuple[Any, Any]] = set()
    for mem in p.fibers.values():
        for i, a in enumerate(mem):
            for b in mem[i + 1 :]:
                out.add(frozenset((value_key(a), value_key(b))))
    return out


def join(a: Partition, b: Partition, name: str) -> Partition:
    """Common refinement: same class iff same class in both."""
    compare(a,b)
    buckets: dict[tuple[Any, Any], list[Any]] = {}
    order: list[tuple[Any, Any]] = []
    seen_elems: list[Any] = []
    for mem in a.fibers.values():
        seen_elems.extend(mem)
    for x in seen_elems:
        key = (a.class_of(x), b.class_of(x))
        if key not in buckets:
            buckets[key] = []
            order.append(key)
        buckets[key].append(x)
    return Partition(name=name, fibers={k: buckets[k] for k in order})


def split_map(fine: Partition, coarse: Partition) -> dict[Any, list[Any]]:
    """coarse label -> fine labels that sit over it."""
    out: dict[Any, list[Any]] = {lab: [] for lab in coarse.labels}
    for flab, fmem in fine.fibers.items():
        if not fmem:
            continue
        clab = coarse.class_of(fmem[0])
        out.setdefault(clab, []).append(flab)
    return out


def ascii_partition(p: Partition, title: str | None = None) -> str:
    title = title or p.name
    cells = []
    for lab, mem in p.fibers.items():
        cells.append(f"{_cell(mem)}:{_lab(lab)}")
    return f"{title:12} " + "  ".join(cells)


def ascii_refinement(fine: Partition, coarse: Partition) -> str:
    rel = compare(fine, coarse)
    lines = [f"refinement  {fine.name}  vs  {coarse.name}   [{rel}]"]
    if rel == "incomparable":
        lines.append("  (no arrow: neither equivalence contains the other)")
        lines.append("  " + ascii_partition(fine))
        lines.append("  " + ascii_partition(coarse))
        return "\n".join(lines)
    if rel == "coarser":
        fine, coarse = coarse, fine
        lines.append("  (displayed with the finer partition on top)")
    sm = split_map(fine, coarse)
    # top: fine cells grouped under each coarse class
    top_groups = []
    bot_cells = []
    guides = []
    for clab, flabs in sm.items():
        fine_cells = [_cell(fine.fibers[f]) for f in flabs]
        group = " ".join(fine_cells)
        top_groups.append(group)
        bot_cells.append(_cell(coarse.fibers[clab]))
        pad = max(len(group), len(bot_cells[-1]))
        guides.append("|" + "-" * max(1, pad - 2) + "|")
    lines.append("  fine   " + "   ".join(top_groups))
    lines.append("         " + "   ".join(guides))
    lines.append("  coarse " + "   ".join(bot_cells))
    lines.append(f"  Q_{fine.name} -->> Q_{coarse.name}")
    return "\n".join(line for line in lines if line is not None)


def ascii_locus(pi: Partition, w: Partition) -> str:
    """Highlight π-classes that split under W."""
    lines = [f"locus  N_{w.name}(π={pi.name})"]
    split_count = 0
    for q, mem in pi.fibers.items():
        wlabs = []
        for x in mem:
            wl = w.class_of(x)
            if wl not in wlabs:
                wlabs.append(wl)
        if len(wlabs) > 1:
            split_count += 1
            parts = []
            for wl in wlabs:
                piece = [x for x in mem if w.class_of(x) == wl]
                parts.append(_cell(piece) + f":W={_lab(wl)}")
            lines.append(f"  SPLIT  π={_lab(q)}  " + " ⊕ ".join(parts))
        else:
            lines.append(f"  clean  π={_lab(q)}  {_cell(mem)}")
    if split_count:
        lines.append(f"  N nonempty: {split_count} of {len(pi.fibers)} labels split")
    else:
        lines.append("  N empty on this carrier  [TESTED_ONLY]")
    return "\n".join(lines)


def ascii_descent_break(pi: Partition, sample: str) -> str:
    return f"descent break  through {pi.name}\n  {sample}"


def atlas(partitions: list[Partition], refinements: list[tuple[str, str]], loci: list[tuple[str, str]]) -> str:
    by = {p.name: p for p in partitions}
    lines = ["-- partition atlas --"]
    for p in partitions:
        lines.append(ascii_partition(p))
    if len(partitions) >= 2:
        a, b = partitions[0], partitions[1]
        j = join(a, b, f"{a.name}∧{b.name}")
        lines.append(ascii_partition(j, title="join"))
        if not refinements:
            lines.append("")
            lines.append(ascii_refinement(a, b))
    for fname, cname in refinements:
        if fname in by and cname in by:
            lines.append("")
            lines.append(ascii_refinement(by[fname], by[cname]))
    for wname, pname in loci:
        if wname in by and pname in by:
            lines.append("")
            lines.append(ascii_locus(by[pname], by[wname]))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# SVG
# ---------------------------------------------------------------------------

PALETTE = [
    "#1d4e89",
    "#7b2d26",
    "#2f6f4e",
    "#8a5a00",
    "#4b3f72",
    "#0b6e6e",
    "#9a3b6a",
    "#3d5a40",
]


def _color(i: int) -> str:
    return PALETTE[i % len(PALETTE)]


def svg_atlas(partitions, loci=None, title='Finite partition atlas', refinements=None):
    """Responsive discrete atlas. Red marks accumulate all supplied locus witnesses."""
    loci, refinements = loci or [], refinements or []
    by = {p.name:p for p in partitions}
    split = {}
    for wname,pname in loci:
        if wname not in by or pname not in by: continue
        witness,pi = by[wname],by[pname]
        compare(witness,pi)
        for label,members in pi.fibers.items():
            if len({value_key(witness.class_of(x)) for x in members})>1:
                split.setdefault(pname,{}).setdefault(value_key(label),[]).append(wname)
    shown = list(partitions)
    if len(partitions)>=2:
        common = join(partitions[0],partitions[1],f'joint({partitions[0].name}, {partitions[1].name})')
        if not any(compare(common,p)=='equal' for p in partitions):
            shown.append(common)
    width,left,cell_w,gap = 1180,254,208,14
    columns = 4
    fragments = []
    def text(x,y,content,size=13,color='#24364b',weight='normal'):
        fragments.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(str(content))}</text>')
    def wrapped(content,chars):
        return textwrap.wrap(str(content),width=chars,break_long_words=True,break_on_hyphens=False) or ['']
    y = 38
    for line in wrapped(title,95):
        text(26,y,line,21,weight='bold'); y += 26
    text(26,y+1,'Finite declared carrier · partitions and verified maps · no continuous shape is inferred',12,'#52657a')
    text(26,y+23,'Red classes split under the witness names shown. Joint rows retain both observations.',12,'#52657a')
    y += 52
    positions = []
    for partition in shown:
        start = y
        labels = list(partition.fibers.items())
        name_lines = wrapped(partition.name,27)
        for j,line in enumerate(name_lines): text(26,start+22+j*17,line,13,weight='bold')
        text(26,start+26+len(name_lines)*17,f'{len(labels)} attained classes',11,'#52657a')
        if not labels:
            text(left,y+22,'Empty partition'); y += 55
        for offset in range(0,len(labels),columns):
            cells = []
            for lab,mem in labels[offset:offset+columns]:
                names = split.get(partition.name,{}).get(value_key(lab),[])
                member_lines = wrapped('  '.join(_lab(x) for x in mem),25)
                label_lines = wrapped(('SPLIT ' if names else 'label ') + _lab(lab),25)
                witness_lines = wrapped('by '+', '.join(names),25) if names else []
                cells.append((lab,names,member_lines,label_lines,witness_lines))
            height = max(66+16*(len(m)+len(l)+len(w)-2) for _,_,m,l,w in cells)
            for index,(lab,names,members,label_lines,witness_lines) in enumerate(cells):
                x = left+index*(cell_w+gap)
                stroke,fill = ('#bb3e32','#fff0eb') if names else ('#99afc2','#f0f6fa')
                fragments.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{height}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="{2 if names else 1}"/>')
                ty = y+22
                for line in members: text(x+12,ty,line,12); ty += 16
                ty += 5
                for line in label_lines: text(x+12,ty,line,11,stroke if names else '#35556b','bold'); ty += 16
                for line in witness_lines: text(x+12,ty,line,10,stroke); ty += 16
                positions.append((x,y,cell_w,height))
            y += height+12
        y = max(y,start+65+len(name_lines)*17)+14
        fragments.append(f'<line x1="26" x2="1150" y1="{y}" y2="{y}" stroke="#dbe4eb"/>')
        y += 20
    relations = list(refinements)
    if not relations and len(partitions)>=2:
        first,second = partitions[:2]
        if compare(first,second)=='coarser': first,second = second,first
        relations = [(first.name,second.name)]
    for fname,cname in relations:
        if fname not in by or cname not in by: continue
        fine,coarse = by[fname],by[cname]
        relation = compare(fine,coarse)
        text(26,y+2,'Requested refinement' if refinements else 'Partition comparison',12,'#52657a')
        y += 26
        if relation not in {'finer','equal'}:
            for line in wrapped(f'{fname} -> {cname}: {relation}; no quotient map in this direction.',105):
                text(26,y,line,13,'#bb3e32'); y += 18
        else:
            left_lines,right_lines = wrapped(f'Q({fname})',42),wrapped(f'Q({cname})',49)
            for j,line in enumerate(left_lines): text(26,y+18*j,line,14,weight='bold')
            for j,line in enumerate(right_lines): text(730,y+18*j,line,14,weight='bold')
            fragments.append(f'<line x1="430" y1="{y-5}" x2="690" y2="{y-5}" stroke="#326b83" stroke-width="2" marker-end="url(#arrow)"/>')
            y += max(len(left_lines),len(right_lines))*18+10
            assignments = '; '.join(f'{_lab(lab)} -> {_lab(coarse.class_of(mem[0]))}' for lab,mem in fine.fibers.items())
            for line in wrapped('Class map: '+assignments,120): text(26,y,line,11,'#52657a'); y += 17
        y += 24
    height = y+18
    head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" font-family="Segoe UI, Arial, sans-serif">',
            f'<title>{escape(title)}</title>',
            '<desc>Exact partitions on the declared finite carrier. Red cells are split by the listed witnesses. Arrows show checked finite quotient maps only.</desc>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#326b83"/></marker></defs>',
            '<rect width="100%" height="100%" fill="#ffffff"/>']
    return '\n'.join(head+fragments+['</svg>'])
