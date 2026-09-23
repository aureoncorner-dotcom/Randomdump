"""Finite implementations of the September 11 locus and prediction calculus.

Every result concerns the declared finite model. No finite hidden-state test here
determines the Markov order of a separately initialized observed process.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from finite import (Carrier,EvalMap,FiniteError,materialize,fibers,locus,
                    refinement_ok,value_key,kernel_pairs)


def joint(carrier: Carrier, *observations: EvalMap, name='joint') -> EvalMap:
    if not observations: raise FiniteError('joint needs at least one observation')
    maps = [materialize(carrier,o) for o in observations]
    if any(o.arity!=1 for o in maps): raise FiniteError('joint observations must be unary')
    return materialize(carrier,EvalMap(name,_fn=lambda x:tuple(o(x) for o in maps)))


def next_output(carrier: Carrier, output: EvalMap, update: EvalMap) -> EvalMap:
    """The witness B after U, with an explicit forward-invariance check."""
    out = materialize(carrier,output)
    step = materialize(carrier,update,closed=True)
    if out.arity!=1 or step.arity!=1: raise FiniteError('next_output needs unary maps')
    return materialize(carrier,EvalMap(f'{output.name}_after_{update.name}',_fn=lambda x:out(step(x))))


def factor(carrier: Carrier, retained: EvalMap, witness: EvalMap) -> dict:
    """Compute the attained factor or retain explicit same-label counterexamples."""
    pi,w = materialize(carrier,retained),materialize(carrier,witness)
    bad = locus(carrier,pi,w)
    return {'status':'counterexample' if bad else 'tested_only',
            'scope':{'carrier':carrier.name,'size':len(carrier),'larger_domain':'unresolved'},
            'counterexamples':bad,
            'factor':None if bad else {q:w(xs[0]) for q,xs in fibers(carrier,pi).items()}}


def minimal_attachments(carrier,retained,witness,coordinates:dict[str,EvalMap]):
    """All inclusion-minimal repairs within the explicitly supplied finite menu."""
    names = list(coordinates)
    if len(names)>12: raise FiniteError('attachment menu limit is 12 coordinates')
    pi,w = materialize(carrier,retained),materialize(carrier,witness)
    menu = {n:materialize(carrier,coordinates[n]) for n in names}
    solutions = []
    for size in range(len(names)+1):
        for subset in combinations(names,size):
            if any(set(prior)<=set(subset) for prior in solutions): continue
            candidate = joint(carrier,pi,*(menu[n] for n in subset))
            if refinement_ok(carrier,candidate,w)[0]: solutions.append(subset)
    return solutions


def autonomous_refinement(carrier,output,update):
    """Coarsest forward-stable partition refining B on a finite deterministic model.

    The returned state-to-class table characterizes necessary distinctions; it
    does not establish that those distinctions are observable at runtime.
    """
    b = materialize(carrier,output)
    u = materialize(carrier,update,closed=True)
    if b.arity!=1 or u.arity!=1: raise FiniteError('autonomy requires unary maps')
    current = b
    for rounds in range(1,len(carrier)+1):
        signatures = joint(carrier,current,next_output(carrier,current,u))
        labels = {value_key(q):i for i,q in enumerate(fibers(carrier,signatures))}
        refined = EvalMap('autonomous_classes',table={x:labels[value_key(signatures(x))] for x in carrier.elements})
        if refinement_ok(carrier,current,refined)[0]:
            return {'partition':refined,'rounds':rounds,
                    'transition':factor(carrier,refined,next_output(carrier,refined,u)),
                    'output':factor(carrier,refined,b),'scope':'declared finite deterministic model'}
        current = refined
    raise FiniteError('partition refinement failed to stabilize')


def representation_gap(carrier,representation,required_objects):
    """Finite image membership is separate from collisions inside fibers."""
    rep = materialize(carrier,representation)
    image = {value_key(q) for q in fibers(carrier,rep)}
    return {'injective_on_carrier':not kernel_pairs(carrier,rep),
            'missing_objects':[x for x in required_objects if value_key(x) not in image],
            'scope':'declared finite representation image'}


def _rational(p):
    if type(p) not in (int,str,Fraction): raise FiniteError('probabilities must be exact integers, rational strings, or Fraction values')
    try: return Fraction(p)
    except (ValueError,ZeroDivisionError) as e: raise FiniteError(f'invalid probability {p!r}') from e


@dataclass
class MarkovKernel:
    carrier: Carrier
    rows: dict

    def __post_init__(self):
        if {value_key(x) for x in self.rows}!={value_key(x) for x in self.carrier.elements}:
            raise FiniteError('kernel must have exactly one row per state')
        checked = {}
        for state in self.carrier.elements:
            row = {}
            for target,p in self.rows[state].items():
                if target not in self.carrier: raise FiniteError('kernel target lies outside carrier')
                probability = _rational(p)
                if probability<0: raise FiniteError('negative probability')
                if probability: row[target] = probability
            if sum(row.values(),Fraction())!=1: raise FiniteError(f'kernel row {state!r} does not sum to 1')
            checked[state] = row
        self.rows = checked

    def next_label_law(self,observation):
        obs = materialize(self.carrier,observation)
        labels = list(fibers(self.carrier,obs))
        table = {}
        for x,row in self.rows.items():
            probabilities = {q:Fraction() for q in labels}
            for y,p in row.items(): probabilities[obs(y)] += p
            table[x] = tuple((q,probabilities[q]) for q in labels)
        return EvalMap('next_label_law',table=table)

    def strong_lumpability(self,observation):
        result = factor(self.carrier,observation,self.next_label_law(observation))
        result['interpretation'] = 'universal finite-state next-label law test; not an observed-history Markov-order test'
        return result

    def future_laws(self,output,horizon):
        """Exact laws of (B_1,...,B_h), including repeated labels, without sampling."""
        if type(horizon)!=int or not 1<=horizon<=8: raise FiniteError('horizon must be an integer in 1–8')
        obs = materialize(self.carrier,output)
        laws = {}
        expansions = 0
        for start in self.carrier.elements:
            live = {(start,()):Fraction(1)}
            for _ in range(horizon):
                following = {}
                for (state,history),mass in live.items():
                    for target,p in self.rows[state].items():
                        expansions += 1
                        if expansions>1_000_000: raise FiniteError('future-law expansion exceeds one million transitions')
                        key = (target,history+(obs(target),))
                        following[key] = following.get(key,Fraction())+mass*p
                live = following
            output_law = {}
            for (_,history),p in live.items(): output_law[history] = output_law.get(history,Fraction())+p
            laws[start] = output_law
        return laws

    def horizon_diameters(self,retained,output,horizon):
        laws = self.future_laws(output,horizon)
        result = {}
        for label,states in fibers(self.carrier,retained).items():
            diameter,best = Fraction(),None
            for x,y in combinations(states,2):
                keys = set(laws[x])|set(laws[y])
                distance = sum((abs(laws[x].get(k,0)-laws[y].get(k,0)) for k in keys),Fraction())/2
                if distance>diameter: diameter,best = distance,(x,y)
            result[label] = {'diameter':diameter,'pair':best,'minimax_lower_bound':diameter/2}
        return {'horizon':horizon,'fibers':result,'scope':'exact supplied finite kernel; not the toroidal unbounded kernel'}
