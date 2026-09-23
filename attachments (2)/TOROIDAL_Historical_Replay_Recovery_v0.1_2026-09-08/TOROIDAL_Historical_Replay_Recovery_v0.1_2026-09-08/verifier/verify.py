"""Supplementary arithmetic checks; the all-orders result is analytical."""
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import json

getcontext().prec = 70

@lru_cache(None)
def normalized_bessel(n):
    # I_n(1) = 2**(-n)/n! * S_n. Avoid tiny absolute Bessel values.
    term = total = D(1)
    for k in range(1, 101):
        term /= D(4*k*(n+k))
        total += term
        if term < D('1e-80'):
            break
    return total

def ratio(n, m):
    n, m = abs(n), abs(m)
    ans = normalized_bessel(m)/normalized_bessel(n)
    for j in range(n+1, m+1):
        ans /= D(2*j)
    for j in range(m+1, n+1):
        ans *= D(2*j)
    return ans

def geometry(L):
    vertices = list(product(range(L), repeat=3))
    edges = [(v,a) for v in vertices for a in range(3)]
    index = {e:i for i,e in enumerate(edges)}
    def shift(v,a):
        w = list(v); w[a] = (w[a]+1)%L
        return tuple(w)
    faces=[]
    for v in vertices:
        for a,b in ((0,1),(0,2),(1,2)):
            faces.append({index[v,a]:1,index[shift(v,a),b]:1,
                          index[shift(v,b),a]:-1,index[v,b]:-1})
    cycles=[]
    for a in range(3):
        cycle={}
        for k in range(L):
            v=[0,0,0];v[a]=k;cycle[index[tuple(v),a]]=1
        cycles.append(cycle)
    return vertices,edges,faces,cycles

def local_two_step(L,N):
    vertices,edges,faces,cycles=geometry(L)
    V=L**3; B=8*V+7
    start=tuple([2*N]*len(edges))
    # Verify the proposed full state has zero divergence and even currents.
    for v in vertices:
        div=0
        for a in range(3):
            pred=list(v);pred[a]=(pred[a]-1)%L
            div += start[edges.index((v,a))]-start[edges.index((tuple(pred),a))]
        assert div == 0
    assert all(i%2==0 for i in start)
    def changed(curr,delta):
        out=list(curr)
        for i,s in delta.items():out[i]+=s
        return tuple(out)
    def acceptance(curr,delta,membrane_factor=D(1)):
        a=membrane_factor
        for i,s in delta.items(): a*=ratio(curr[i],curr[i]+s)
        return min(D(1),a)
    @lru_cache(None)
    def survival(curr):
        out=D(1)
        for cycle in cycles:
            for sign in (-1,1):
                delta={i:sign*v for i,v in cycle.items()}
                out-=acceptance(curr,delta)/D(2*B)
        return out
    u=survival(start)
    # Identity, cube and sheet moves leave currents and q unchanged.
    # Thus their contribution to A^2 1 is their total proposal weight * u,
    # regardless of membrane acceptance or rejection.
    a2=D(2*V+1)/D(B)*u
    total_weight=F(2*V+1,B)
    for faceset,scale,membrane_factor in ((faces,1,D('0.5')),
                                          (faces,2,D(1)),
                                          (cycles,2,D(1))):
        for move in faceset:
            for sign in (-1,1):
                delta={i:sign*scale*v for i,v in move.items()}
                a=acceptance(start,delta,membrane_factor)
                a2+=((1-a)*u+a*survival(changed(start,delta)))/D(2*B)
                total_weight+=F(1,2*B)
    # Accepted unit cycles leave the killed sector; rejected ones stay.
    for cycle in cycles:
        for sign in (-1,1):
            a=acceptance(start,{i:sign*v for i,v in cycle.items()})
            a2+=(1-a)*u/D(2*B)
            total_weight+=F(1,2*B)
    assert total_weight == 1
    eps=D(4*N)**(-L)
    r0=D(1)-D(3)/D(2*B)
    return {'L':L,'N':N,'A1':str(u),'A2_over_A1':str(a2/u),
            'scaled_correction':str((a2/u-r0)/eps),
            'predicted_limit':str(-D(3)/D(2*B))}

def clock_check(L,d):
    B=8*L**3+7
    r=sum((F(comb(3,j),8)*F(B-j,B)**d for j in range(4)),F(0))
    derivative=-F(d,8*B)*sum((comb(3,j)*j*F(B-j,B)**(d-1)
                              for j in range(1,4)),F(0))
    assert r>0 and derivative<0
    # Independent exact group-walk convolution, with differentiated weights.
    c=F(1,2*B)
    p={0:1-3*c,1:c,2:c,4:c}
    dp={0:-3*c,1:c,2:c,4:c}
    vec=[F(1)]+[F(0)]*7; der=[F(0)]*8
    for _ in range(d):
        vec,der=([sum((vec[x^z]*p[z] for z in p),F(0)) for x in range(8)],
                 [sum((der[x^z]*p[z]+vec[x^z]*dp[z] for z in p),F(0))
                  for x in range(8)])
    assert vec[0]==r and der[0]==derivative
    return {'L':L,'B':B,'spacing':d,'r0':float(r),
            'derivative_at_zero':float(derivative),
            'exact_convolution_agrees':True}

if __name__=='__main__':
    result={'scope':'Supplementary exact group arithmetic and decimal local checks; no sampler replay',
            'clock_checks':[clock_check(L,d) for L in (2,3,4)
                            for d in (1,8*L**3+7)],
            'local_checks':[local_two_step(2,N) for N in (10,100,1000)]}
    print(json.dumps(result,indent=2))
