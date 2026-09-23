"""PRIME MEANIE V — TORUS SHOCK.

Portable, standard-library math challenge for a voice conversation.
--voice emits short challenge cards; --answers emits their answer key.
Default output is a deterministic JSON report; --verify recomputes a report.
No microphone, audio routing, network, or host-application changes are made.
This is a math/execution probe, not a means to override an assistant's rules.
Receipt hashes check reproducibility and file identity, not who executed code.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from dataclasses import dataclass
from decimal import Decimal,localcontext
from fractions import Fraction
from pathlib import Path

PROBE_ID = "PRIME-MEANIE-V-TORUS-SHOCK-857"
MOD = 65521
SHAPE = (5,7,11)

PILOT_SNAPSHOT = {'source_sha256': '10c997e5be3bd31b0fafc2db74f25676933051e38fc2cd6694aa2c7a0d761298', 'date': '2026-09-06', 'physical_Q2': 'UNRESOLVED', 'sizes': [{'L': 2, 'pilot_screen': 'PASS', 'worst_signed_W_Rhat': 1.0039509805796922, 'minimum_signed_W_ESS': 2344.2029004509086, 'all_chains_visited_all_sectors': True}, {'L': 3, 'pilot_screen': 'UNRESOLVED', 'worst_signed_W_Rhat': 1.0155100810334254, 'minimum_signed_W_ESS': 741.2365559650594, 'all_chains_visited_all_sectors': True}, {'L': 4, 'pilot_screen': 'UNRESOLVED', 'worst_signed_W_Rhat': 1.0346902319355458, 'minimum_signed_W_ESS': 336.00675227090704, 'all_chains_visited_all_sectors': True}]}

@dataclass(frozen=True)
class Q5:
    """a + b sqrt(5), with exact rational coefficients and exact ordering."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    @staticmethod
    def cast(value):
        return value if isinstance(value, Q5) else Q5(value)

    def __add__(self, other):
        other = self.cast(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        other = self.cast(other)
        return Q5(self.a * other.a + 5 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.cast(other)
        denominator = other.a * other.a - 5 * other.b * other.b
        if not denominator:
            raise ZeroDivisionError("zero Q5 denominator")
        return self * Q5(other.a / denominator, -other.b / denominator)

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if not a or (a > 0) == (b > 0):
            return (b > 0) - (b < 0)
        d = a * a - 5 * b * b
        return ((a > 0) - (a < 0)) * ((d > 0) - (d < 0))

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __le__(self, other):
        return (self - other).sign() <= 0

    def __gt__(self, other):
        return (self - other).sign() > 0

    def __ge__(self, other):
        return (self - other).sign() >= 0

    def floor(self):
        # sqrt(5) lies strictly between 2 and 3. Binary search uses no floats.
        p, q = self.a + 2 * self.b, self.a + 3 * self.b
        lo, hi = math.floor(min(p, q)), math.floor(max(p, q)) + 1
        while hi - lo > 1:
            middle = (lo + hi) // 2
            if self < middle:
                hi = middle
            else:
                lo = middle
        return lo

    def ceil(self):
        return -(-self).floor()

    def frac(self):
        return self - self.floor()

    def as_dict(self):
        return {"a": str(self.a), "b": str(self.b)}

    def decimal(self, places=25):
        # Extra guard digits also handle cancellation in large coefficients.
        digits = max(len(str(abs(v))) for f in (self.a, self.b)
                     for v in (f.numerator, f.denominator))
        with localcontext() as ctx:
            ctx.prec = places + 25 + digits
            a = Decimal(self.a.numerator) / Decimal(self.a.denominator)
            b = Decimal(self.b.numerator) / Decimal(self.b.denominator)
            return format(a + b * Decimal(5).sqrt(), f".{places}f")

    def approximate(self):
        return float(self.decimal())


ALPHA = Q5(Fraction(3, 2), Fraction(-1, 2))
TAU = 15 - 39 * ALPHA



def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('utf-8')


def least_factor(n):
    if n<2:return None
    if n%2==0:return 2
    for d in range(3,math.isqrt(n)+1,2):
        if n%d==0:return d
    return n


def strong_pass(n,base):
    if n<2:return False
    if n in (2,3):return True
    if n%2==0:return False
    base%=n
    if base==0:return True  # Non-informative base; this alone proves nothing.
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    x=pow(base,d,n)
    if x in (1,n-1):return True
    for _ in range(s-1):
        x=x*x%n
        if x==n-1:return True
    return False


def prime_stream(count):
    result=[];n=2
    while len(result)<count:
        prime=True
        for p in result:
            if p*p>n:break
            if n%p==0:prime=False;break
        if prime:result.append(n)
        n+=1
    return result


def primes_report(challenge):
    candidate=100001+2*(int.from_bytes(hashlib.sha256(challenge.encode()).digest()[:2],'big')%10000)
    rows=[]
    for n in (31,121,341,561,30031,10050017,3215031751,candidate):
        f=least_factor(n);remaining=n;factors=[]
        while remaining>1:
            divisor=least_factor(remaining);factors.append(divisor);remaining//=divisor
        rows.append({'n':n,'prime':f==n,'least_factor':f,'cofactor':n//f,
                     'prime_factors':factors,
                     'strong_tests':{str(b):strong_pass(n,b) for b in (2,3,5,7,11)}})
    return {'checks':rows,'same_mod30':[31%30,121%30],
            'lesson':'A residue match or a few probable-prime passes is not a primality proof. Trial division certifies these bounded inputs.'}


def constants_report():
    phi=Q5(Fraction(1,2),Fraction(1,2));p,q=1,0
    for _ in range(13):p,q=p+2*q,p+q
    partial=sum((Fraction(1,math.factorial(k)) for k in range(31)),Fraction(0))
    first=Fraction(1,math.factorial(31));upper=partial+first/(1-Fraction(1,32))
    n=2**53
    return {'golden':{'phi':phi.as_dict(),'phi_squared_minus_phi_minus_one':(phi*phi-phi-1).as_dict(),
                     'alpha':ALPHA.as_dict(),'slip_threshold_tau':TAU.as_dict(),'tau_decimal_display':TAU.decimal(30)},
        'silver':{'expression':'(1+sqrt(2))^13 = p+q*sqrt(2)','p':p,'q':q,'pell_residual':p*p-2*q*q},
        'e_enclosure':{'lower':str(partial),'upper':str(upper),'width':str(upper-partial),
                       'proof':'Positive exponential series through 30; subsequent term ratios are <=1/32.'},
        'floating_display':{'pi':math.pi,'e':math.e,'status':'binary floating approximations, not exact constants'},
        'precision_trap':{'exact_integer_gap':(n+1)-n,'float_gap':float(n+1)-float(n),
            'rational_decimal_sum':str(Fraction('0.1')+Fraction('0.2')),'float_decimal_sum_equals_0_3':.1+.2==.3}}


def observe(theta):
    scaled=39*theta;b=scaled.floor();rho=scaled-b
    slip=int(rho<TAU);nxt=(theta+ALPHA).frac();nb=(39*nxt).floor()
    if (nb-b)%39!=15-slip:raise ArithmeticError('Departure identity failed')
    return {'bin':b,'strand':b%3,'rho':rho.as_dict(),'slip':slip,'jump':(nb-b)%39,'next_bin':nb}


def phase_report(challenge,steps):
    numerator=int.from_bytes(hashlib.sha256(challenge.encode()).digest()[:8],'big')%MOD
    initial=Q5(Fraction(numerator,MOD));theta=initial;rho0=(39*theta).frac()
    slips=0;indices=[];trace=hashlib.sha256();checkpoints=[]
    prime_indices=set(prime_stream(steps))
    for n in range(steps):
        row=observe(theta);slips+=row['slip']
        if row['slip']:indices.append(n)
        trace.update(canonical({'n':n,**row})+b'\n')
        if n in prime_indices and len(checkpoints)<12:checkpoints.append({'n':n,**row})
        theta=(theta+ALPHA).frac()
    rhon=(39*theta).frac();residual=Q5(slips)-steps*TAU-rhon+rho0
    deviation=Q5(slips)-steps*TAU
    if residual!=Q5(0) or not -1<deviation<1:raise ArithmeticError('Slip count identity failed')
    epsilon=Q5(Fraction(1,10**40))
    boundaries=[{'rho':x.as_dict(),'slip':int(x<TAU)} for x in (Q5(0),TAU-epsilon,TAU,TAU+epsilon)]
    witness=[observe(Q5(0)),observe(TAU/39)]
    return {'steps':steps,'theta0':initial.as_dict(),'slips':slips,'count_identity_residual':residual.as_dict(),
        'count_deviation':deviation.as_dict(),'absolute_deviation_less_than_one':True,
        'complete_gap_lengths':sorted(set(b-a for a,b in zip(indices,indices[1:]))),
        'prime_index_checkpoints':checkpoints,'trace_sha256':trace.hexdigest(),'boundary_checks':boundaries,
        'same_visible_bin_different_next_bin':witness,
        'scope':'Exact irrational rotation, not a mixing process or a physical Q2 simulation.'}


MOVES={'X':(0,1),'x':(0,-1),'Y':(1,1),'y':(1,-1),'Z':(2,1),'z':(2,-1)}


def torus_walk(word,shape=SHAPE):
    position=[0]*3;lift=[0]*3;wraps=[0]*3;eta_xor=[0]*3;crossings=[0]*3
    for letter in word:
        a,sign=MOVES[letter];old=wraps[a];lift[a]+=sign
        crossings[a]+=(position[a]+sign)//shape[a]
        position[a]=(position[a]+sign)%shape[a]
        wraps[a]=lift[a]//shape[a];eta_xor[a]^=(wraps[a]-old)&1
    if crossings!=wraps or eta_xor!=[w&1 for w in wraps]:raise ArithmeticError('Lift cocycle failed')
    return {'endpoint':position,'integer_lift':lift,'signed_wraps':wraps,'wrap_parity':eta_xor,
            'closed':position==[0,0,0],'cut_crossing_sums':crossings}


def geometry_report(challenge,steps):
    digest=hashlib.sha256(challenge.encode()).digest();primes=prime_stream(steps)
    letters='XYZ';word=''.join((letters[(p+digest[(i+7)%32])%3] if digest[i%32]&1 else letters[(p+digest[(i+7)%32])%3].lower()) for i,p in enumerate(primes))
    direct=torus_walk(word);endpoint_by_counts=[sum(MOVES[x][1] for x in word if MOVES[x][0]==a)%SHAPE[a] for a in range(3)]
    if endpoint_by_counts!=direct['endpoint']:raise ArithmeticError('Independent endpoint failed')
    witnesses=[{'name':name,**torus_walk(w)} for name,w in [('stationary',''),('two_positive_x_loops','X'*10),('two_negative_x_loops','x'*10)]]
    return {'shape':SHAPE,'prime_driven_steps':steps,'word_sha256':hashlib.sha256(word.encode()).hexdigest(),'path':direct,
        'independent_endpoint':endpoint_by_counts,'same_endpoint_and_parity_different_signed_wraps':witnesses,
        'scope':'Open-path wraps are lift-dependent crossing counts. Only closed paths define torus winding. This walk is not the field sampler.'}


def matrix_mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in (0,1))%MOD for i in (0,1) for j in (0,1))


def path_matrix(word):
    steps={'R':(1,1,0,1),'L':(1,-1,0,1),'U':(1,0,1,1),'D':(1,0,-1,1)}
    matrix=(1,0,0,1)
    for letter in word:matrix=matrix_mul(steps[letter],matrix)
    columns=[]
    for x,y in ((1,0),(0,1)):
        for letter in word:
            if letter=='R':x+=y
            elif letter=='L':x-=y
            elif letter=='U':y+=x
            else:y-=x
            x%=MOD;y%=MOD
        columns.append((x,y))
    independent=(columns[0][0],columns[1][0],columns[0][1],columns[1][1])
    if matrix!=independent or (matrix[0]*matrix[3]-matrix[1]*matrix[2])%MOD!=1:raise ArithmeticError('Matrix replay failed')
    return matrix


def cocycle_report():
    rows=[{'word':w,'matrix':path_matrix(w)} for w in ('','RU','UR','RULD','RL')]
    return {'modulus':MOD,'step_order':'new step multiplies on the left','paths':rows,
        'RU_equals_UR':path_matrix('RU')==path_matrix('UR'),
        'scope':'Assigned ordered matrix updates. A contractible RULD loop can have nonidentity product; this is not a torus homotopy invariant.'}


def report(challenge='857',steps=857):
    if not isinstance(challenge,str) or not 1<=len(challenge)<=256:raise ValueError('Challenge must have 1 through 256 characters')
    if type(steps) is not int or not 1<=steps<=10000:raise ValueError('Steps must be 1 through 10000')
    result={'receipt':{'probe_id':PROBE_ID,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'challenge':challenge,'steps':steps,'interpretation':'Reproducible computation receipt; not proof of executor identity or access to a hidden pipeline.'},
        'prime_gauntlet':primes_report(challenge),'constant_forge':constants_report(),'phase_39':phase_report(challenge,steps),
        'prime_torus':geometry_report(challenge,steps),'ordered_cocycle':cocycle_report(),
        'huge_integer':{'expression':'2**136279841-1','last12':f'{(pow(2,136279841,10**12)-1)%10**12:012d}',
                        'mod857':(pow(2,136279841,857)-1)%857,'mod65521':(pow(2,136279841,MOD)-1)%MOD,'primality_tested':False},
        'q2_checkpoint':PILOT_SNAPSHOT}
    result['receipt']['section_names']=list(result)[1:]
    result['seal_sha256']=hashlib.sha256(canonical(result)).hexdigest()
    return result


def voice_cards(challenge,steps):
    return f'''PRIME MEANIE V — TORUS SHOCK
VOICE CHALLENGE | nonce={challenge!r} | steps={steps}

Read one round at a time. Keep answers short, then explain the key distinction.
If using the Python file, label executed output separately from mental reasoning.
The challenge text is a nonce, not an instruction to execute.

ROUND 1 / PRIME IMPOSTOR
31 and 121 have the same remainder modulo 30. Are both prime?
Now factor 3,215,031,751. Does passing strong tests at bases 2, 3, 5, and 7 settle primality?

ROUND 2 / CONSTANT FORGE
Let phi=(1+sqrt(5))/2. Evaluate phi squared minus phi minus one exactly.
For (1+sqrt(2)) to the thirteenth power, find integers p and q and evaluate p squared minus 2 q squared.
What does floating arithmetic do to (2 to the 53 plus one) minus (2 to the 53)?

ROUND 3 / THE 39-PHASE EDGE
Alpha=(3-sqrt(5))/2; tau=15-39 alpha. A slip means rho is strictly below tau.
At rho equal to tau, is this a slip? Can two states in bin zero have different next bins?
Explain why knowing the bin is weaker than knowing the phase.

ROUND 4 / SIGNED TORUS
On a 5 by 7 by 11 torus, compare staying still, ten positive x steps, and ten negative x steps.
They have the same endpoint and wrap parity. What information distinguishes them?

ROUND 5 / ORDER MATTERS
Apply R:(x,y)->(x+y,y) and U:(x,y)->(x,x+y), with the new step acting on the left.
Do RU and UR have the same matrix? Is a nonidentity RULD product automatically a nontrivial torus homotopy class?

ROUND 6 / GIANT WITHOUT EXPANSION
For 2 to the 136,279,841 minus one, compute the last twelve decimal digits and its remainder modulo 857.
Does either result prove the number prime?

FINAL BOSS / PARITY IS NOT THE WHOLE STATE
Our L=4 pilot visited every parity sector, yet signed winding had R-hat 1.03469 and minimum ESS about 336.
Has the full chain passed the pilot mixing screen? What should the next run target?

EXECUTION CHECK
With the attached file, run this challenge and step count; return the report's section names and seal.
If execution is unavailable, say so. A copied or recomputed seal does not identify who executed the code.
'''


def answer_key(r):
    silver=r['constant_forge']['silver'];phase=r['phase_39'];huge=r['huge_integer']
    composite=next(x for x in r['prime_gauntlet']['checks'] if x['n']==3215031751)
    return {'1':f"31 is prime; 121=11*11. 3215031751={'*'.join(map(str,composite['prime_factors']))}; four strong passes do not prove primality.",
        '2':f"Golden residual 0; silver p={silver['p']}, q={silver['q']}, Pell residual={silver['pell_residual']}. Exact integer gap 1; float gap 0.",
        '3':{'at_threshold_slip':0,'same_bin_next_bins':[x['next_bin'] for x in phase['same_visible_bin_different_next_bin']],
             'nonce_run_slips':phase['slips'],'explanation':'The missing within-bin phase changes the successor.'},
        '4':'Signed wraps are (0,0,0), (2,0,0), (-2,0,0). Endpoint and parity discard magnitude and sign.',
        '5':{'RU':path_matrix('RU'),'UR':path_matrix('UR'),'explanation':'The assigned matrix transport is order-sensitive and is not a torus homotopy invariant.'},
        '6':{'last12':huge['last12'],'mod857':huge['mod857'],'primality_proved':False},
        'final_boss':'No. Parity diagnostics passed, but signed winding failed the broader screen. Longer signed-winding runs are next; no physical Q2 verdict follows.',
        'receipt_seal':r['seal_sha256']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--challenge',default='857');parser.add_argument('--steps',type=int,default=857)
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--voice',action='store_true');mode.add_argument('--answers',action='store_true');mode.add_argument('--verify',type=Path)
    parser.add_argument('--out',type=Path,help='Write to a new file; never overwrite an existing one')
    args=parser.parse_args()
    try:
        if args.verify:
            if args.verify.stat().st_size>2000000:raise ValueError('Report exceeds 2 MB')
            saved=json.loads(args.verify.read_text(encoding='utf-8'))
            expected=report(saved['receipt']['challenge'],saved['receipt']['steps'])
            if canonical(saved)!=canonical(expected):raise ValueError('Report differs from full recomputation with this source file')
            output=json.dumps({'status':'VERIFIED','seal_sha256':expected['seal_sha256'],'identity_attested':False},indent=2)
        else:
            result=report(args.challenge,args.steps)
            output=voice_cards(args.challenge,args.steps) if args.voice else json.dumps(answer_key(result) if args.answers else result,indent=2)
        if args.out:
            with args.out.open('x',encoding='utf-8',newline='\n') as f:f.write(output+'\n')
        else:print(output)
    except (ValueError,KeyError,TypeError,OSError) as error:parser.exit(2,f'ERROR: {error}\n')


if __name__=='__main__':main()
