# Geometry and atomic-number bridge — executed checks

8 September 2026 · CC0-1.0 · Independent equation-level implementation

**Outcome:** 500,000 checked phase transitions passed. The onsite symmetry check recovered the first allowed phase-dependent terms at degree six. An exploratory atomic-number indexing supplied no preference for prime numbers in phase-averaged counts. This establishes a reproducible computational check of specified mathematics; a physical atomic/material test remains NOT_RUN.

## What was run

The latest Geometry Maximization v2.0 equations were implemented independently in Python. This was not a rerun of the author's `geometry_reference.py`, which is referenced by a relative link in the document. No L=2/L=3 sampler, physical Q2 experiment, or chemical measurement was run here. Existing records were not edited.

Before execution, the script fixed five starting phases, 100,000 departures per start, a monomial enumeration through total degree 24, and one exploratory atomic indexing convention. No starting phase was selected to maximize a prime association. These design choices were recorded in the script before its first run; this is a local analysis plan, not an externally registered experiment.

Exact comparisons use numbers `(a+b*sqrt(5))/1092`. Floating-point arithmetic proposes a floor; exact integer sign comparisons correct it. Branch decisions and the reported identities therefore do not depend on floating-point boundary rounding. Reported decimal phase averages are approximations.

## Phase results

The implemented constants are alpha=(3-sqrt(5))/2 and tau=(39*sqrt(5)-87)/2. The checked departing transition is j=15-sigma, with sigma=1 when 0<=rho<tau. Each step checks the full phase against the reduced rho, strand, and z updates, the cumulative slip identity, and the strict error bound |S_N-N*tau|<1.

| Starting phase | Departures | Slips | Complete gap lengths | Checked identities |
|---|---:|---:|---|---|
| zero | 100,000 | 10,333 | 9, 10 | PASS |
| one_seventh | 100,000 | 10,332 | 9, 10 | PASS |
| alpha | 100,000 | 10,332 | 9, 10 | PASS |
| rho_equals_tau | 100,000 | 10,333 | 9, 10 | PASS |
| bin_boundary_13_over_39 | 100,000 | 10,333 | 9, 10 | PASS |

For theta0=0, the source checkpoints were also reproduced: 5 slips in 39 departures, 53 in 507, and 1,034 in 10,000. The rho=0 endpoint gives a slip; rho=tau does not.

An exact bin-only closure counterexample was constructed: theta=0 and theta=1/78 both occupy bin 0, but their next bins are 14 and 15. Retaining the phase resolves this specific ambiguity. The finite runs check the stated formulas; they are not new proofs of every global minimality, nonmixing, or algebraic claim in the source.

## Symmetry result and its possible physical use

For the field model's onsite monomial z^p conjugate(z)^r, invariance under the declared sign identification and order-three action requires p+r even and p-r divisible by three. Because p+r and p-r have the same parity, these conditions are exactly equivalent to p-r divisible by six. This elementary equivalence holds for all nonnegative p,r; the executable enumeration checked all 325 monomials through total degree 24 with zero discrepancies.

The first phase-dependent terms are z^6 and conjugate(z)^6. With the physical variable Phi=z^2, their sum is Phi^3+conjugate(Phi)^3. For z=R exp(i psi), it is 2 R^6 cos(6 psi). Thus a possible physical bridge would be an experimentally identified order parameter with these transformation rules and a measured angular response. Sixfold symmetry in this model follows from the assumed transformations. It is not a measurement of an atom or a prediction that atomic number six is special. The phase-screen coordinate also named z and the field order parameter named z belong to different models; shared notation does not identify them.

A prospective material test would first identify an observable and independently justify its transformation under the sign and order-three actions. It would then specify the measured response, angular reference, temperature/field conditions, sampling design, errors, and competing lower-harmonic terms. Symmetry permits a sixth-order coefficient but does not require it to be nonzero or dominate. The current documents do not supply that material-specific map or a calibrated coefficient, so no numerical material prediction was invented here.

## Exploratory atomic-number mapping

**Analyst-added assumption:** index the model departures by n=Z-1 for atomic numbers Z=1 through 118, using a slip to mark an element. Start at rho0=0 for the default display. The source model does not prescribe this identification, an atomic origin phase, or a chemical interpretation of a slip. This exercise addresses the simplest direct numbering proposal only; it does not stand in for all possible links between geometry and atomic structure.

The default mapping marks Z=1, 10, 20, 30, 39, 49, 59, 68, 78, 88, 97, 107, 117. Three of these thirteen labels are prime: 59, 97, 107. The full interval 1..118 contains thirty primes.

To check origin sensitivity exhaustively, partition rho0 in [0,1) at every breakpoint {k*tau}, k=0..118. This yields 119 open cells. The program checks one exact midpoint per cell and every boundary, preserving the half-open convention. These points cover all possible slip-label patterns for this finite indexing.

Across the cells, 12 or 13 elements are marked; between 1 and 6 of them have prime atomic numbers. Under a uniformly distributed starting phase, every Z has the same slip probability tau, because its marking set is a translated interval of length tau. Consequently:

- Expected marked prime labels: 30*tau, approximately 3.09976684.
- Expected marked labels overall: 118*tau, approximately 12.19241623.
- Ratio of those expected counts: 30/118, approximately 25.4237%, exactly the prime fraction of the index set.

That last quantity is the ratio of expectations, not the expectation of a per-phase fraction. No p-value or physical randomness model is claimed. The calculation shows no built-in prime preference in phase-averaged counts under this assumed mapping. It does not refute a different specified observable, material mechanism, or independently fixed phase.

## Relation to the materials discussed

Atomic-number labels, prime factors, chemical bonding, and model symmetries are separate quantities. The relevant labels are:

| Element | Atomic number Z | Prime factorization |
|---|---:|---|
| Beryllium | 4 | 2^2 |
| Carbon | 6 | 2*3 |
| Nitrogen | 7 | 7 |
| Oxygen | 8 | 2^3 |
| Silicon | 14 | 2*7 |
| Lanthanum | 57 | 3*19 |
| Uranium | 92 | 2^2*23 |

Source: [NIST atomic-number table](https://physics.nist.gov/PhysRefData/Handbook/atomic_number.htm). The [NIST periodic-table page](https://www.nist.gov/pml/periodic-table-elements) provides the complete element table. Factorizations were calculated arithmetically. No abundance or spectrum was used as an input.

This run cannot identify HED material as BeLaU, establish nitrogen bonding in a fulgurite, or connect a meteor trajectory to composition. The HED evidence gate remains new published trajectory/radiant evidence for geometry and fall-linked recovered-material classification/analysis for composition. The historical HED denominator, pairing, and common-stream claim receive no upgrade from this computation.

## Sources and execution scope

- [Geometry Maximization v2.0, dated September 6](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit), retrieved September 8; source metadata modified September 8 at 01:22:43.179 UTC. Sections 2–3 supplied phase equations, checks, and boundary convention.
- [Field Theory Update v0.3, dated September 6](https://docs.google.com/document/d/1gGxdHa0Sg9EIKtIJTnI3u0M8emQXwI6rMuZoH82E-TM/edit), retrieved September 8. Section 1 supplied the onsite transformation rules and physical field Phi=z^2. Its historical sampler status is not treated as the status of later validation records.
- NIST links above support atomic labels. All other numeric findings in this report were computed in this run.

The independent script finished successfully with all assertions passing. The full results, source code, atomic-label table, and exhaustive phase-cell output are embedded below so this single report preserves a reproducible record. Save the Python block as `run.py` and execute `python3 run.py`; it writes its outputs beside itself. This report's prose does not expand the checked scope to the entire geometry program.

Script SHA-256: `30ba2afb9c62977b4d206598de2f31b3376c11d738a9b6897be878593cc6b898`.

## Machine-readable results

```json
{
  "scope": "Independent equation-level checks; not the author's reference executable.\nCC0-1.0. Python standard library only. Run: python3 run.py\nAll classification comparisons are exact in Q(sqrt(5)); floats only suggest floors.\nFrozen scope before first execution: five 100000-departure starts, degree<=24\nonsite monomials, and n=Z-1 for Z=1..118 with an exhaustive initial-phase sweep.\nThe atomic mapping is an analyst-added exploratory assumption, not source theory.\n",
  "denominator": 1092,
  "departures_per_start": 100000,
  "runs": [
    {
      "start": "zero",
      "exact_theta0": "(0 + (0)*sqrt(5))/1092",
      "checkpoints": {
        "39": 5,
        "507": 53,
        "10000": 1034,
        "100000": 10333
      },
      "gaps": [
        9,
        10
      ],
      "status": "PASS"
    },
    {
      "start": "one_seventh",
      "exact_theta0": "(156 + (0)*sqrt(5))/1092",
      "checkpoints": {
        "39": 4,
        "507": 52,
        "10000": 1033,
        "100000": 10332
      },
      "gaps": [
        9,
        10
      ],
      "status": "PASS"
    },
    {
      "start": "alpha",
      "exact_theta0": "(1638 + (-546)*sqrt(5))/1092",
      "checkpoints": {
        "39": 4,
        "507": 52,
        "10000": 1033,
        "100000": 10332
      },
      "gaps": [
        9,
        10
      ],
      "status": "PASS"
    },
    {
      "start": "rho_equals_tau",
      "exact_theta0": "(-1218 + (546)*sqrt(5))/1092",
      "checkpoints": {
        "39": 4,
        "507": 53,
        "10000": 1034,
        "100000": 10333
      },
      "gaps": [
        9,
        10
      ],
      "status": "PASS"
    },
    {
      "start": "bin_boundary_13_over_39",
      "exact_theta0": "(364 + (0)*sqrt(5))/1092",
      "checkpoints": {
        "39": 5,
        "507": 53,
        "10000": 1034,
        "100000": 10333
      },
      "gaps": [
        9,
        10
      ],
      "status": "PASS"
    }
  ],
  "bin_only_witness": {
    "initial_bins": [
      0,
      0
    ],
    "successor_bins": [
      14,
      15
    ],
    "theta0": [
      "(0 + (0)*sqrt(5))/1092",
      "(14 + (0)*sqrt(5))/1092"
    ]
  },
  "onsite_symmetry": {
    "monomials_checked": 325,
    "max_total_degree": 24,
    "mismatches": [],
    "lowest_phase_dependent_degree": 6,
    "degree_six_terms": [
      [
        0,
        6
      ],
      [
        6,
        0
      ]
    ]
  },
  "atomic_mapping": {
    "definition": "n=Z-1; rho0=0; departure slip marks Z",
    "status": "EXPLORATORY_LABEL_MAPPING_ONLY",
    "Z_range": [
      1,
      118
    ],
    "prime_count": 30,
    "default_slip_Z": [
      1,
      10,
      20,
      30,
      39,
      49,
      59,
      68,
      78,
      88,
      97,
      107,
      117
    ],
    "default_prime_slip_Z": [
      59,
      97,
      107
    ]
  },
  "phase_sensitivity": {
    "open_cells": 119,
    "boundaries_checked": 119,
    "slip_count_range": [
      12,
      13
    ],
    "prime_slip_count_range": [
      1,
      6
    ],
    "uniform_phase_expected_prime_slips": 3.099766837377118,
    "uniform_phase_expected_all_slips": 12.192416227016693,
    "ratio_of_expected_prime_to_all_slips": 0.2542372881355932,
    "interpretation": "Every Z has identical phase-averaged slip probability tau. No prime enrichment in the phase-averaged counts under this mapping. Not a test of spectra, bonding, or every possible atomic mapping."
  },
  "script_sha256": "30ba2afb9c62977b4d206598de2f31b3376c11d738a9b6897be878593cc6b898"
}
```

## Executed Python source

```python
"""Independent equation-level checks; not the author's reference executable.
CC0-1.0. Python standard library only. Run: python3 run.py
All classification comparisons are exact in Q(sqrt(5)); floats only suggest floors.
Frozen scope before first execution: five 100000-departure starts, degree<=24
onsite monomials, and n=Z-1 for Z=1..118 with an exhaustive initial-phase sweep.
The atomic mapping is an analyst-added exploratory assumption, not source theory.
"""
import math, json, hashlib, csv
from pathlib import Path
from functools import cmp_to_key

ROOT=Path(__file__).resolve().parent
D=1092
ZERO=(0,0); ONE=(D,0)
ALPHA=(3*D//2,-D//2)
TAU=(-87*D//2,39*D//2)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,n): return (x[0]*n,x[1]*n)
def sign(x):
    a,b=x
    if b==0: return (a>0)-(a<0)
    if a==0: return (b>0)-(b<0)
    if a>0 and b>0: return 1
    if a<0 and b<0: return -1
    c=a*a-5*b*b
    return ((c>0)-(c<0)) if a>0 else -((c>0)-(c<0))
def floorq(x):
    k=math.floor((x[0]+x[1]*math.sqrt(5))/D)
    while sign((x[0]-k*D,x[1]))<0: k-=1
    while sign((x[0]-(k+1)*D,x[1]))>=0: k+=1
    return k
def frac(x): return sub(x,mul(ONE,floorq(x)))
def dec(x): return (x[0]+x[1]*math.sqrt(5))/D
def exactstr(x): return f'({x[0]} + ({x[1]})*sqrt(5))/{D}'
def slip(rho): return int(sign(sub(rho,TAU))<0)
def prime(z): return z>=2 and all(z%k for k in range(2,math.isqrt(z)+1))

starts={'zero':ZERO,'one_seventh':(D//7,0),'alpha':ALPHA,
        'rho_equals_tau':(-87*D//78,D//2),'bin_boundary_13_over_39':(D//3,0)}
N=100000
results={'scope':__doc__,'denominator':D,'departures_per_start':N,'runs':[]}
assert frac(mul(starts['rho_equals_tau'],39))==TAU
assert slip(ZERO)==1 and slip(TAU)==0
for name,start in starts.items():
    theta=start; b=floorq(mul(theta,39)); rho=frac(mul(theta,39)); rho0=rho
    s=b%3; z=frac(mul(theta,13)); total=0; last=None; gaps=set(); checkpoints={}
    for n in range(N):
        sig=slip(rho)
        next_theta=frac(add(theta,ALPHA))
        bn=floorq(mul(next_theta,39)); rn=frac(mul(next_theta,39)); sn=bn%3
        assert (bn-b)%39==15-sig
        assert rn==add(sub(rho,TAU),mul(ONE,sig))
        assert sn==(s-sig)%3
        zn=frac(mul(next_theta,13))
        assert frac(sub(z,(TAU[0]//3,TAU[1]//3)))==zn
        assert mul(z,3)==add(mul(ONE,s),rho)
        total+=sig
        assert mul(ONE,total)==add(mul(TAU,n+1),sub(rn,rho0))
        err=sub(mul(ONE,total),mul(TAU,n+1))
        assert sign(sub(ONE,err))>0 and sign(add(ONE,err))>0
        if sig:
            if last is not None: gaps.add(n-last)
            last=n
        if n+1 in (39,507,10000,100000): checkpoints[str(n+1)]=total
        theta,b,rho,s,z=next_theta,bn,rn,sn,zn
    assert gaps=={9,10}
    results['runs'].append({'start':name,'exact_theta0':exactstr(start),'checkpoints':checkpoints,'gaps':sorted(gaps),'status':'PASS'})

# Construct an exact failure of bin-only closure: same bin 0, different next bins.
x=ZERO; y=(D//39,0) # y/2 stays in bin zero, above the slip threshold.
y=(y[0]//2,0)
results['bin_only_witness']={'initial_bins':[floorq(mul(x,39)),floorq(mul(y,39))],
    'successor_bins':[floorq(mul(frac(add(x,ALPHA)),39)),floorq(mul(frac(add(y,ALPHA)),39))],
    'theta0':[exactstr(x),exactstr(y)]}
assert results['bin_only_witness']['initial_bins']==[0,0]
assert results['bin_only_witness']['successor_bins']==[14,15]

# Onsite invariance check: sign identification plus global order-three rotation.
monomials=[]; mismatches=[]
for degree in range(25):
    for p in range(degree+1):
        r=degree-p
        inv=((p+r)%2==0 and (p-r)%3==0)
        if inv!=((p-r)%6==0): mismatches.append([p,r])
        if inv and p!=r: monomials.append([p,r])
assert not mismatches
results['onsite_symmetry']={'monomials_checked':sum(range(1,26)),'max_total_degree':24,
    'mismatches':mismatches,'lowest_phase_dependent_degree':min(p+r for p,r in monomials),
    'degree_six_terms':[[p,r] for p,r in monomials if p+r==6]}

# Atomic-number indexing: an explicit assumption, not a prediction of chemistry.
primes=[z for z in range(1,119) if prime(z)]
def atom_rows(initial_rho):
    return [{'Z':z,'prime':prime(z),'slip':slip(frac(sub(initial_rho,mul(TAU,z-1))))} for z in range(1,119)]
rows=atom_rows(ZERO)
with (ROOT/'atomic_labels.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
default_slips=[r['Z'] for r in rows if r['slip']]
results['atomic_mapping']={'definition':'n=Z-1; rho0=0; departure slip marks Z',
    'status':'EXPLORATORY_LABEL_MAPPING_ONLY','Z_range':[1,118],'prime_count':len(primes),
    'default_slip_Z':default_slips,'default_prime_slip_Z':[z for z in default_slips if prime(z)]}

# Every label changes only at rho0={k*tau}, k=0..118.
# Test all 119 open cells and every boundary; no phase is optimized or selected.
breaks=sorted(set(frac(mul(TAU,k)) for k in range(119)),key=cmp_to_key(lambda x,y:sign(sub(x,y))))
phase_rows=[]; total_width=ZERO; weighted_prime=ZERO
for i,lo in enumerate(breaks):
    hi=breaks[i+1] if i+1<len(breaks) else ONE
    summed=add(lo,hi); assert summed[0]%2==0 and summed[1]%2==0
    mid=(summed[0]//2,summed[1]//2); width=sub(hi,lo)
    rr=atom_rows(mid); ss=[r['Z'] for r in rr if r['slip']]; pp=[z for z in ss if prime(z)]
    br=atom_rows(lo)
    # Half-open convention makes the boundary agree with its right-hand cell.
    assert [r['slip'] for r in br]==[r['slip'] for r in rr]
    total_width=add(total_width,width);weighted_prime=add(weighted_prime,mul(width,len(pp)))
    phase_rows.append({'lo':exactstr(lo),'hi':exactstr(hi),'width_approx':dec(width),'slip_count':len(ss),'prime_slip_count':len(pp),'prime_slip_Z':pp})
assert total_width==ONE
assert weighted_prime==mul(TAU,len(primes))
results['phase_sensitivity']={'open_cells':len(phase_rows),'boundaries_checked':len(breaks),
    'slip_count_range':[min(r['slip_count'] for r in phase_rows),max(r['slip_count'] for r in phase_rows)],
    'prime_slip_count_range':[min(r['prime_slip_count'] for r in phase_rows),max(r['prime_slip_count'] for r in phase_rows)],
    'uniform_phase_expected_prime_slips':dec(weighted_prime),
    'uniform_phase_expected_all_slips':dec(mul(TAU,118)),
    'ratio_of_expected_prime_to_all_slips':len(primes)/118,
    'interpretation':'Every Z has identical phase-averaged slip probability tau. No prime enrichment in the phase-averaged counts under this mapping. Not a test of spectra, bonding, or every possible atomic mapping.'}
(ROOT/'phase_cells.json').write_text(json.dumps(phase_rows,indent=2)+'\n')
results['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
```

## Atomic-label output

```csv
Z,prime,slip
1,False,1
2,True,0
3,True,0
4,False,0
5,True,0
6,False,0
7,True,0
8,False,0
9,False,0
10,False,1
11,True,0
12,False,0
13,True,0
14,False,0
15,False,0
16,False,0
17,True,0
18,False,0
19,True,0
20,False,1
21,False,0
22,False,0
23,True,0
24,False,0
25,False,0
26,False,0
27,False,0
28,False,0
29,True,0
30,False,1
31,True,0
32,False,0
33,False,0
34,False,0
35,False,0
36,False,0
37,True,0
38,False,0
39,False,1
40,False,0
41,True,0
42,False,0
43,True,0
44,False,0
45,False,0
46,False,0
47,True,0
48,False,0
49,False,1
50,False,0
51,False,0
52,False,0
53,True,0
54,False,0
55,False,0
56,False,0
57,False,0
58,False,0
59,True,1
60,False,0
61,True,0
62,False,0
63,False,0
64,False,0
65,False,0
66,False,0
67,True,0
68,False,1
69,False,0
70,False,0
71,True,0
72,False,0
73,True,0
74,False,0
75,False,0
76,False,0
77,False,0
78,False,1
79,True,0
80,False,0
81,False,0
82,False,0
83,True,0
84,False,0
85,False,0
86,False,0
87,False,0
88,False,1
89,True,0
90,False,0
91,False,0
92,False,0
93,False,0
94,False,0
95,False,0
96,False,0
97,True,1
98,False,0
99,False,0
100,False,0
101,True,0
102,False,0
103,True,0
104,False,0
105,False,0
106,False,0
107,True,1
108,False,0
109,True,0
110,False,0
111,False,0
112,False,0
113,True,0
114,False,0
115,False,0
116,False,0
117,False,1
118,False,0
```

## Exhaustive phase cells

```json
[
  {
    "lo": "(0 + (0)*sqrt(5))/1092",
    "hi": "(-4618614 + (2065518)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      59,
      97,
      107
    ]
  },
  {
    "lo": "(-4618614 + (2065518)*sqrt(5))/1092",
    "hi": "(-3237780 + (1447992)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      59,
      107
    ]
  },
  {
    "lo": "(-3237780 + (1447992)*sqrt(5))/1092",
    "hi": "(-1856946 + (830466)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      59,
      107
    ]
  },
  {
    "lo": "(-1856946 + (830466)*sqrt(5))/1092",
    "hi": "(-476112 + (212940)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      59,
      107
    ]
  },
  {
    "lo": "(-476112 + (212940)*sqrt(5))/1092",
    "hi": "(-5094726 + (2278458)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      59,
      107
    ]
  },
  {
    "lo": "(-5094726 + (2278458)*sqrt(5))/1092",
    "hi": "(-3713892 + (1660932)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      11,
      59
    ]
  },
  {
    "lo": "(-3713892 + (1660932)*sqrt(5))/1092",
    "hi": "(-2333058 + (1043406)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      59,
      79
    ]
  },
  {
    "lo": "(-2333058 + (1043406)*sqrt(5))/1092",
    "hi": "(-952224 + (425880)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      59,
      79
    ]
  },
  {
    "lo": "(-952224 + (425880)*sqrt(5))/1092",
    "hi": "(-5570838 + (2491398)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      59,
      79
    ]
  },
  {
    "lo": "(-5570838 + (2491398)*sqrt(5))/1092",
    "hi": "(-4190004 + (1873872)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      59,
      79
    ]
  },
  {
    "lo": "(-4190004 + (1873872)*sqrt(5))/1092",
    "hi": "(-2809170 + (1256346)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      11,
      59,
      79,
      89
    ]
  },
  {
    "lo": "(-2809170 + (1256346)*sqrt(5))/1092",
    "hi": "(-1428336 + (638820)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      11,
      79,
      89
    ]
  },
  {
    "lo": "(-1428336 + (638820)*sqrt(5))/1092",
    "hi": "(-47502 + (21294)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      11,
      31,
      79,
      89
    ]
  },
  {
    "lo": "(-47502 + (21294)*sqrt(5))/1092",
    "hi": "(-4666116 + (2086812)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      11,
      31,
      79,
      89
    ]
  },
  {
    "lo": "(-4666116 + (2086812)*sqrt(5))/1092",
    "hi": "(-3285282 + (1469286)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      11,
      31,
      79,
      89
    ]
  },
  {
    "lo": "(-3285282 + (1469286)*sqrt(5))/1092",
    "hi": "(-1904448 + (851760)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      11,
      31,
      79,
      89
    ]
  },
  {
    "lo": "(-1904448 + (851760)*sqrt(5))/1092",
    "hi": "(-523614 + (234234)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 6,
    "prime_slip_Z": [
      2,
      11,
      31,
      41,
      79,
      89
    ]
  },
  {
    "lo": "(-523614 + (234234)*sqrt(5))/1092",
    "hi": "(-5142228 + (2299752)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      79,
      89
    ]
  },
  {
    "lo": "(-5142228 + (2299752)*sqrt(5))/1092",
    "hi": "(-3761394 + (1682226)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 6,
    "prime_slip_Z": [
      2,
      31,
      41,
      79,
      89,
      109
    ]
  },
  {
    "lo": "(-3761394 + (1682226)*sqrt(5))/1092",
    "hi": "(-2380560 + (1064700)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      89,
      109
    ]
  },
  {
    "lo": "(-2380560 + (1064700)*sqrt(5))/1092",
    "hi": "(-999726 + (447174)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      89,
      109
    ]
  },
  {
    "lo": "(-999726 + (447174)*sqrt(5))/1092",
    "hi": "(-5618340 + (2512692)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 13,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      89,
      109
    ]
  },
  {
    "lo": "(-5618340 + (2512692)*sqrt(5))/1092",
    "hi": "(-4237506 + (1895166)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      89,
      109
    ]
  },
  {
    "lo": "(-4237506 + (1895166)*sqrt(5))/1092",
    "hi": "(-2856672 + (1277640)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      2,
      31,
      41,
      109
    ]
  },
  {
    "lo": "(-2856672 + (1277640)*sqrt(5))/1092",
    "hi": "(-1475838 + (660114)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      2,
      31,
      41,
      61,
      109
    ]
  },
  {
    "lo": "(-1475838 + (660114)*sqrt(5))/1092",
    "hi": "(-95004 + (42588)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      2,
      41,
      61,
      109
    ]
  },
  {
    "lo": "(-95004 + (42588)*sqrt(5))/1092",
    "hi": "(-4713618 + (2108106)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      41,
      61,
      109
    ]
  },
  {
    "lo": "(-4713618 + (2108106)*sqrt(5))/1092",
    "hi": "(-3332784 + (1490580)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      41,
      61,
      109
    ]
  },
  {
    "lo": "(-3332784 + (1490580)*sqrt(5))/1092",
    "hi": "(-1951950 + (873054)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      3,
      41,
      61,
      71,
      109
    ]
  },
  {
    "lo": "(-1951950 + (873054)*sqrt(5))/1092",
    "hi": "(-571116 + (255528)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      61,
      71,
      109
    ]
  },
  {
    "lo": "(-571116 + (255528)*sqrt(5))/1092",
    "hi": "(-5189730 + (2321046)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      3,
      13,
      61,
      71,
      109
    ]
  },
  {
    "lo": "(-5189730 + (2321046)*sqrt(5))/1092",
    "hi": "(-3808896 + (1703520)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      13,
      61,
      71
    ]
  },
  {
    "lo": "(-3808896 + (1703520)*sqrt(5))/1092",
    "hi": "(-2428062 + (1085994)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      13,
      61,
      71
    ]
  },
  {
    "lo": "(-2428062 + (1085994)*sqrt(5))/1092",
    "hi": "(-1047228 + (468468)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      13,
      61,
      71
    ]
  },
  {
    "lo": "(-1047228 + (468468)*sqrt(5))/1092",
    "hi": "(-4285008 + (1916460)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      3,
      13,
      23,
      61,
      71
    ]
  },
  {
    "lo": "(-4285008 + (1916460)*sqrt(5))/1092",
    "hi": "(-2904174 + (1298934)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 5,
    "prime_slip_Z": [
      3,
      13,
      23,
      61,
      71
    ]
  },
  {
    "lo": "(-2904174 + (1298934)*sqrt(5))/1092",
    "hi": "(-1523340 + (681408)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      13,
      23,
      71
    ]
  },
  {
    "lo": "(-1523340 + (681408)*sqrt(5))/1092",
    "hi": "(-142506 + (63882)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      3,
      13,
      23,
      71
    ]
  },
  {
    "lo": "(-142506 + (63882)*sqrt(5))/1092",
    "hi": "(-4761120 + (2129400)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      13,
      23,
      71
    ]
  },
  {
    "lo": "(-4761120 + (2129400)*sqrt(5))/1092",
    "hi": "(-3380286 + (1511874)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      13,
      23,
      71,
      101
    ]
  },
  {
    "lo": "(-3380286 + (1511874)*sqrt(5))/1092",
    "hi": "(-1999452 + (894348)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      13,
      23,
      101
    ]
  },
  {
    "lo": "(-1999452 + (894348)*sqrt(5))/1092",
    "hi": "(-618618 + (276822)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      13,
      23,
      43,
      101
    ]
  },
  {
    "lo": "(-618618 + (276822)*sqrt(5))/1092",
    "hi": "(-5237232 + (2342340)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      23,
      43,
      101
    ]
  },
  {
    "lo": "(-5237232 + (2342340)*sqrt(5))/1092",
    "hi": "(-3856398 + (1724814)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      23,
      43,
      101
    ]
  },
  {
    "lo": "(-3856398 + (1724814)*sqrt(5))/1092",
    "hi": "(-2475564 + (1107288)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      23,
      43,
      101
    ]
  },
  {
    "lo": "(-2475564 + (1107288)*sqrt(5))/1092",
    "hi": "(-1094730 + (489762)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      23,
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-1094730 + (489762)*sqrt(5))/1092",
    "hi": "(-4332510 + (1937754)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-4332510 + (1937754)*sqrt(5))/1092",
    "hi": "(-2951676 + (1320228)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-2951676 + (1320228)*sqrt(5))/1092",
    "hi": "(-1570842 + (702702)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-1570842 + (702702)*sqrt(5))/1092",
    "hi": "(-190008 + (85176)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-190008 + (85176)*sqrt(5))/1092",
    "hi": "(-4808622 + (2150694)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      5,
      43,
      53,
      101
    ]
  },
  {
    "lo": "(-4808622 + (2150694)*sqrt(5))/1092",
    "hi": "(-3427788 + (1533168)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      43,
      53
    ]
  },
  {
    "lo": "(-3427788 + (1533168)*sqrt(5))/1092",
    "hi": "(-2046954 + (915642)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      5,
      43,
      53,
      73
    ]
  },
  {
    "lo": "(-2046954 + (915642)*sqrt(5))/1092",
    "hi": "(-666120 + (298116)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      53,
      73
    ]
  },
  {
    "lo": "(-666120 + (298116)*sqrt(5))/1092",
    "hi": "(-5284734 + (2363634)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      53,
      73
    ]
  },
  {
    "lo": "(-5284734 + (2363634)*sqrt(5))/1092",
    "hi": "(-3903900 + (1746108)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      53,
      73
    ]
  },
  {
    "lo": "(-3903900 + (1746108)*sqrt(5))/1092",
    "hi": "(-2523066 + (1128582)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      5,
      53,
      73,
      83
    ]
  },
  {
    "lo": "(-2523066 + (1128582)*sqrt(5))/1092",
    "hi": "(-1142232 + (511056)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      73,
      83
    ]
  },
  {
    "lo": "(-1142232 + (511056)*sqrt(5))/1092",
    "hi": "(-4380012 + (1959048)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      73,
      83
    ]
  },
  {
    "lo": "(-4380012 + (1959048)*sqrt(5))/1092",
    "hi": "(-2999178 + (1341522)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      73,
      83
    ]
  },
  {
    "lo": "(-2999178 + (1341522)*sqrt(5))/1092",
    "hi": "(-1618344 + (723996)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      73,
      83
    ]
  },
  {
    "lo": "(-1618344 + (723996)*sqrt(5))/1092",
    "hi": "(-237510 + (106470)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      5,
      73,
      83
    ]
  },
  {
    "lo": "(-237510 + (106470)*sqrt(5))/1092",
    "hi": "(-4856124 + (2171988)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      73,
      83
    ]
  },
  {
    "lo": "(-4856124 + (2171988)*sqrt(5))/1092",
    "hi": "(-3475290 + (1554462)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      73,
      83,
      103
    ]
  },
  {
    "lo": "(-3475290 + (1554462)*sqrt(5))/1092",
    "hi": "(-2094456 + (936936)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      83,
      103
    ]
  },
  {
    "lo": "(-2094456 + (936936)*sqrt(5))/1092",
    "hi": "(-713622 + (319410)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      83,
      103
    ]
  },
  {
    "lo": "(-713622 + (319410)*sqrt(5))/1092",
    "hi": "(-5332236 + (2384928)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      83,
      103
    ]
  },
  {
    "lo": "(-5332236 + (2384928)*sqrt(5))/1092",
    "hi": "(-3951402 + (1767402)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      83,
      103,
      113
    ]
  },
  {
    "lo": "(-3951402 + (1767402)*sqrt(5))/1092",
    "hi": "(-2570568 + (1149876)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-2570568 + (1149876)*sqrt(5))/1092",
    "hi": "(-1189734 + (532350)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-1189734 + (532350)*sqrt(5))/1092",
    "hi": "(-4427514 + (1980342)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-4427514 + (1980342)*sqrt(5))/1092",
    "hi": "(-3046680 + (1362816)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-3046680 + (1362816)*sqrt(5))/1092",
    "hi": "(-1665846 + (745290)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-1665846 + (745290)*sqrt(5))/1092",
    "hi": "(-285012 + (127764)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      103,
      113
    ]
  },
  {
    "lo": "(-285012 + (127764)*sqrt(5))/1092",
    "hi": "(-4903626 + (2193282)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      7,
      103,
      113
    ]
  },
  {
    "lo": "(-4903626 + (2193282)*sqrt(5))/1092",
    "hi": "(-3522792 + (1575756)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      113
    ]
  },
  {
    "lo": "(-3522792 + (1575756)*sqrt(5))/1092",
    "hi": "(-2141958 + (958230)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      113
    ]
  },
  {
    "lo": "(-2141958 + (958230)*sqrt(5))/1092",
    "hi": "(-761124 + (340704)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      113
    ]
  },
  {
    "lo": "(-761124 + (340704)*sqrt(5))/1092",
    "hi": "(-5379738 + (2406222)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      7,
      17,
      113
    ]
  },
  {
    "lo": "(-5379738 + (2406222)*sqrt(5))/1092",
    "hi": "(-3998904 + (1788696)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-3998904 + (1788696)*sqrt(5))/1092",
    "hi": "(-2618070 + (1171170)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-2618070 + (1171170)*sqrt(5))/1092",
    "hi": "(-1237236 + (553644)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-1237236 + (553644)*sqrt(5))/1092",
    "hi": "(-4475016 + (2001636)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-4475016 + (2001636)*sqrt(5))/1092",
    "hi": "(-3094182 + (1384110)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-3094182 + (1384110)*sqrt(5))/1092",
    "hi": "(-1713348 + (766584)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      7,
      17
    ]
  },
  {
    "lo": "(-1713348 + (766584)*sqrt(5))/1092",
    "hi": "(-332514 + (149058)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      7,
      17,
      37
    ]
  },
  {
    "lo": "(-332514 + (149058)*sqrt(5))/1092",
    "hi": "(-4951128 + (2214576)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      17,
      37
    ]
  },
  {
    "lo": "(-4951128 + (2214576)*sqrt(5))/1092",
    "hi": "(-3570294 + (1597050)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      17,
      37
    ]
  },
  {
    "lo": "(-3570294 + (1597050)*sqrt(5))/1092",
    "hi": "(-2189460 + (979524)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      17,
      37
    ]
  },
  {
    "lo": "(-2189460 + (979524)*sqrt(5))/1092",
    "hi": "(-808626 + (361998)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      17,
      37,
      47
    ]
  },
  {
    "lo": "(-808626 + (361998)*sqrt(5))/1092",
    "hi": "(-5427240 + (2427516)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-5427240 + (2427516)*sqrt(5))/1092",
    "hi": "(-4046406 + (1809990)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-4046406 + (1809990)*sqrt(5))/1092",
    "hi": "(-2665572 + (1192464)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-2665572 + (1192464)*sqrt(5))/1092",
    "hi": "(-1284738 + (574938)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-1284738 + (574938)*sqrt(5))/1092",
    "hi": "(-4522518 + (2022930)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-4522518 + (2022930)*sqrt(5))/1092",
    "hi": "(-3141684 + (1405404)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      37,
      47
    ]
  },
  {
    "lo": "(-3141684 + (1405404)*sqrt(5))/1092",
    "hi": "(-1760850 + (787878)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      37,
      47,
      67
    ]
  },
  {
    "lo": "(-1760850 + (787878)*sqrt(5))/1092",
    "hi": "(-380016 + (170352)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      47,
      67
    ]
  },
  {
    "lo": "(-380016 + (170352)*sqrt(5))/1092",
    "hi": "(-4998630 + (2235870)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      47,
      67
    ]
  },
  {
    "lo": "(-4998630 + (2235870)*sqrt(5))/1092",
    "hi": "(-3617796 + (1618344)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      47,
      67
    ]
  },
  {
    "lo": "(-3617796 + (1618344)*sqrt(5))/1092",
    "hi": "(-2236962 + (1000818)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      47,
      67
    ]
  },
  {
    "lo": "(-2236962 + (1000818)*sqrt(5))/1092",
    "hi": "(-856128 + (383292)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 1,
    "prime_slip_Z": [
      67
    ]
  },
  {
    "lo": "(-856128 + (383292)*sqrt(5))/1092",
    "hi": "(-5474742 + (2448810)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      19,
      67
    ]
  },
  {
    "lo": "(-5474742 + (2448810)*sqrt(5))/1092",
    "hi": "(-4093908 + (1831284)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      19,
      67
    ]
  },
  {
    "lo": "(-4093908 + (1831284)*sqrt(5))/1092",
    "hi": "(-2713074 + (1213758)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      19,
      67
    ]
  },
  {
    "lo": "(-2713074 + (1213758)*sqrt(5))/1092",
    "hi": "(-1332240 + (596232)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 2,
    "prime_slip_Z": [
      19,
      67
    ]
  },
  {
    "lo": "(-1332240 + (596232)*sqrt(5))/1092",
    "hi": "(-4570020 + (2044224)*sqrt(5))/1092",
    "width_approx": 0.026138164721354298,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      19,
      29,
      67
    ]
  },
  {
    "lo": "(-4570020 + (2044224)*sqrt(5))/1092",
    "hi": "(-3189186 + (1426698)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      19,
      29,
      67,
      97
    ]
  },
  {
    "lo": "(-3189186 + (1426698)*sqrt(5))/1092",
    "hi": "(-1808352 + (809172)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      19,
      29,
      97
    ]
  },
  {
    "lo": "(-1808352 + (809172)*sqrt(5))/1092",
    "hi": "(-427518 + (191646)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      19,
      29,
      97
    ]
  },
  {
    "lo": "(-427518 + (191646)*sqrt(5))/1092",
    "hi": "(-5046132 + (2257164)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      19,
      29,
      97
    ]
  },
  {
    "lo": "(-5046132 + (2257164)*sqrt(5))/1092",
    "hi": "(-3665298 + (1639638)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      19,
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-3665298 + (1639638)*sqrt(5))/1092",
    "hi": "(-2284464 + (1022112)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      19,
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-2284464 + (1022112)*sqrt(5))/1092",
    "hi": "(-903630 + (404586)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      19,
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-903630 + (404586)*sqrt(5))/1092",
    "hi": "(-5522244 + (2470104)*sqrt(5))/1092",
    "width_approx": 0.02257944085215638,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-5522244 + (2470104)*sqrt(5))/1092",
    "hi": "(-4141410 + (1852578)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-4141410 + (1852578)*sqrt(5))/1092",
    "hi": "(-2760576 + (1235052)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      29,
      97,
      107
    ]
  },
  {
    "lo": "(-2760576 + (1235052)*sqrt(5))/1092",
    "hi": "(-1379742 + (617526)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 4,
    "prime_slip_Z": [
      29,
      59,
      97,
      107
    ]
  },
  {
    "lo": "(-1379742 + (617526)*sqrt(5))/1092",
    "hi": "(1092 + (0)*sqrt(5))/1092",
    "width_approx": 0.003558723868771487,
    "slip_count": 12,
    "prime_slip_count": 3,
    "prime_slip_Z": [
      59,
      97,
      107
    ]
  }
]
```
