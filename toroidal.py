"""Integer cut flux for a finite periodic cubic lattice; no sampler or memory theorem."""
from itertools import product
from finite import FiniteError

def vertices(shape):
    if len(shape)!=3 or any(type(n)!=int or n<2 or n>32 for n in shape):
        raise FiniteError('shape must have three integer lengths in 2–32')
    return list(product(*(range(n) for n in shape)))

def checked_current(shape,current):
    sites = vertices(shape)
    allowed = {(v,axis) for v in sites for axis in range(3)}
    for edge,value in current.items():
        if edge not in allowed or type(value)!=int: raise FiniteError('current must assign integers to declared positive edges')
    return {edge:current.get(edge,0) for edge in allowed}

def divergence(shape,current):
    current = checked_current(shape,current)
    div = {v:0 for v in vertices(shape)}
    for (v,axis),value in current.items():
        target = list(v); target[axis] = (target[axis]+1)%shape[axis]; target = tuple(target)
        div[v] += value
        div[target] -= value
    return div

def cut_fluxes(shape,current):
    current = checked_current(shape,current)
    return tuple(tuple(sum(value for (v,a),value in current.items() if a==axis and v[axis]==cut)
                       for cut in range(shape[axis])) for axis in range(3))

def signed_winding(shape,current):
    if any(divergence(shape,current).values()): raise FiniteError('signed winding requires zero divergence; use modular_flux for compatible sourced states')
    cuts = cut_fluxes(shape,current)
    if any(len(set(axis))!=1 for axis in cuts): raise FiniteError('parallel cut sums disagree')
    return tuple(axis[0] for axis in cuts)

def modular_flux(shape,current,modulus=6):
    if type(modulus)!=int or modulus<2: raise FiniteError('modulus must be an integer >=2')
    if any(d%modulus for d in divergence(shape,current).values()): raise FiniteError('divergence is incompatible with the declared modulus')
    cuts = cut_fluxes(shape,current)
    if any(len({v%modulus for v in axis})!=1 for axis in cuts): raise FiniteError('modular cut flux is not invariant')
    return tuple(axis[0]%modulus for axis in cuts)

def reference_cycles(shape,winding):
    vertices(shape)
    if len(winding)!=3 or any(type(w)!=int for w in winding): raise FiniteError('winding needs three integers')
    current = {}
    for axis,value in enumerate(winding):
        for n in range(shape[axis]):
            v = [0,0,0]; v[axis] = n
            current[(tuple(v),axis)] = value
    return current
