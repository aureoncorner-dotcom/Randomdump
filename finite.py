"""Exact finite maps with totality, closure, and bounded evaluation checks."""
from __future__ import annotations
import ast
import itertools
import operator
import keyword
import shlex
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable

MAX_INPUTS = 100_000
MAX_ELEMENTS = 512

class FiniteError(ValueError):
    """Invalid finite model; report as a diagnostic."""

def validate_value(v):
    if type(v) in (bool,int,str,type(None)) or isinstance(v,Fraction):
        if isinstance(v,Fraction) and max(v.numerator.bit_length(),v.denominator.bit_length())>4096:
            raise FiniteError('rational numerator or denominator exceeds 4096 bits')
        if isinstance(v,int) and v.bit_length()>4096:
            raise FiniteError('integer exceeds 4096 bits')
        if isinstance(v,str) and len(v)>4096:
            raise FiniteError('string exceeds 4096 characters')
        return v
    if isinstance(v,tuple) and len(v)<=128:
        for x in v: validate_value(x)
        return v
    raise FiniteError(f'unsupported finite value: {type(v).__name__}; use exact scalars or tuples')

def value_key(v):
    validate_value(v)
    if isinstance(v,tuple): return ('tuple',tuple(value_key(x) for x in v))
    if isinstance(v,Fraction): return ('rational',v.numerator,v.denominator)
    return (type(v).__name__,v)

def _ensure_dict_keys(values):
    seen = {}
    for v in values:
        key = value_key(v)
        if v in seen and seen[v]!=key:
            raise FiniteError(f'Python-equal labels of different types: {v!r}; use explicit string labels')
        seen[v] = key

BINOPS = {ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,
          ast.FloorDiv:operator.floordiv,ast.Mod:operator.mod,ast.BitAnd:operator.and_,
          ast.BitOr:operator.or_,ast.BitXor:operator.xor}
COMPARE = {ast.Eq:operator.eq,ast.NotEq:operator.ne,ast.Lt:operator.lt,
           ast.LtE:operator.le,ast.Gt:operator.gt,ast.GtE:operator.ge}
UNARY = {ast.USub:operator.neg,ast.UAdd:operator.pos,ast.Not:operator.not_}
FUNCTIONS = {'abs':abs,'int':int,'str':str,'min':min,'max':max,'rat':Fraction,
             'parity':lambda x:x%2,'mod2':lambda x:x%2,'mod4':lambda x:x%4,'floor2':lambda x:x//2}

def compile_expr(expr):
    if len(expr)>4096: raise FiniteError('formula exceeds 4096 characters')
    try: tree = ast.parse(expr,mode='eval')
    except (SyntaxError,ValueError,RecursionError) as e: raise FiniteError(f'invalid formula: {e}') from e
    nodes = list(ast.walk(tree))
    if len(nodes)>256: raise FiniteError('formula is too complex')
    allowed = (ast.Expression,ast.Constant,ast.Name,ast.Load,ast.BinOp,ast.UnaryOp,
               ast.Compare,ast.BoolOp,ast.And,ast.Or,ast.Call,ast.Tuple,ast.IfExp,
               *BINOPS,*COMPARE,*UNARY)
    for node in nodes:
        if not isinstance(node,allowed): raise FiniteError(f'disallowed expression form: {type(node).__name__}')
        if isinstance(node,ast.Constant): validate_value(node.value)
        if isinstance(node,ast.Call) and (not isinstance(node.func,ast.Name) or node.func.id not in FUNCTIONS or node.keywords):
            raise FiniteError('only documented named functions with positional arguments are allowed')
    def ev(n,env):
        if isinstance(n,ast.Expression): return ev(n.body,env)
        if isinstance(n,ast.Constant): return n.value
        if isinstance(n,ast.Name):
            if n.id not in env: raise FiniteError(f'unbound name `{n.id}`')
            return env[n.id]
        if isinstance(n,ast.Tuple): return tuple(ev(x,env) for x in n.elts)
        if isinstance(n,ast.UnaryOp): return validate_value(UNARY[type(n.op)](ev(n.operand,env)))
        if isinstance(n,ast.BinOp):
            a,b = ev(n.left,env),ev(n.right,env)
            if isinstance(n.op,ast.Mult):
                for seq,count in ((a,b),(b,a)):
                    if isinstance(seq,(str,tuple)) and isinstance(count,int) and len(seq)*max(0,count)>4096:
                        raise FiniteError('sequence multiplication exceeds evaluation limit')
            return validate_value(BINOPS[type(n.op)](a,b))
        if isinstance(n,ast.Compare):
            left = ev(n.left,env)
            for op,right_node in zip(n.ops,n.comparators):
                right = ev(right_node,env)
                if not COMPARE[type(op)](left,right): return False
                left = right
            return True
        if isinstance(n,ast.BoolOp):
            result = isinstance(n.op,ast.And)
            for child in n.values:
                if isinstance(n.op,ast.And) and not result: break
                if isinstance(n.op,ast.Or) and result: break
                result = ev(child,env)
            return result
        if isinstance(n,ast.IfExp): return ev(n.body if ev(n.test,env) else n.orelse,env)
        if isinstance(n,ast.Call): return validate_value(FUNCTIONS[n.func.id](*(ev(a,env) for a in n.args)))
        raise FiniteError('unsupported expression')
    def run(env):
        try: return validate_value(ev(tree,env))
        except FiniteError: raise
        except (ArithmeticError,TypeError,ValueError,RecursionError) as e:
            raise FiniteError(f'formula evaluation failed: {type(e).__name__}: {e}') from e
    return run

def parse_atom(tok):
    tok = tok.strip()
    if tok.lower() in {'true','yes'}: return True
    if tok.lower() in {'false','no'}: return False
    if tok.startswith(('"',"'",'(')):
        try: return validate_value(ast.literal_eval(tok))
        except (SyntaxError,ValueError,TypeError) as e: raise FiniteError(f'invalid literal {tok!r}') from e
    try: return int(tok)
    except ValueError: return tok

def parse_element_list(text):
    lexer = shlex.shlex(text,posix=False)
    lexer.whitespace += ','
    lexer.whitespace_split = True
    lexer.commenters = ''
    return [parse_atom(p) for p in lexer]

@dataclass
class Carrier:
    name: str
    elements: list[Any]
    def __post_init__(self):
        self.elements = list(self.elements)
        if not self.elements or len(self.elements)>MAX_ELEMENTS: raise FiniteError(f'carrier needs 1–{MAX_ELEMENTS} elements')
        keys = [value_key(x) for x in self.elements]
        if len(set(keys))!=len(keys): raise FiniteError('carrier contains duplicate elements')
        _ensure_dict_keys(self.elements)
        self._keys = set(keys)
    def __contains__(self,x): return value_key(x) in self._keys
    def __len__(self): return len(self.elements)

@dataclass
class EvalMap:
    name: str
    params: list[str] = field(default_factory=lambda:['x'])
    formula: str | None = None
    table: dict[Any,Any] = field(default_factory=dict)
    _fn: Callable | None = field(default=None,repr=False)
    @property
    def arity(self): return len(self.params)
    def bind(self):
        if not 1<=self.arity<=8 or len(set(self.params))!=self.arity: raise FiniteError(f'{self.name}: need 1–8 distinct parameters')
        if any(not p.isidentifier() or keyword.iskeyword(p) for p in self.params):
            raise FiniteError(f'{self.name}: invalid parameter name')
        if self.formula is not None and self.table: raise FiniteError(f'{self.name}: use formula or table, not both')
        if self.formula is not None:
            compiled = compile_expr(self.formula)
            self._fn = lambda *args:compiled(dict(zip(self.params,args)))
        elif self.table:
            typed = {value_key(k):v for k,v in self.table.items()}
            def lookup(*args):
                key = args[0] if self.arity==1 else args
                if value_key(key) not in typed: raise FiniteError(f'{self.name}: no table entry for {key!r}')
                return typed[value_key(key)]
            self._fn = lookup
        elif self._fn is None: raise FiniteError(f'{self.name}: neither formula nor table')
    def __call__(self,*args):
        if len(args)!=self.arity: raise FiniteError(f'{self.name}: expected {self.arity} arguments, got {len(args)}')
        if self._fn is None: self.bind()
        try: return validate_value(self._fn(*args))
        except FiniteError: raise
        except (ArithmeticError,TypeError,ValueError,KeyError,RecursionError) as e: raise FiniteError(f'{self.name}: evaluation failed: {e}') from e

def input_tuples(carrier,arity):
    if not 1<=arity<=8 or len(carrier)**arity>MAX_INPUTS: raise FiniteError(f'evaluation exceeds {MAX_INPUTS} inputs')
    return itertools.product(carrier.elements,repeat=arity)

def materialize(carrier,em,*,closed=False):
    table = {}
    for args in input_tuples(carrier,em.arity):
        v = em(*args)
        if closed and v not in carrier: raise FiniteError(f'{em.name}{args!r}={v!r} lies outside carrier {carrier.name}')
        table[args[0] if em.arity==1 else args] = v
    _ensure_dict_keys(table.values())
    return EvalMap(em.name,list(em.params),table=table)

def fibers(carrier,obs):
    if obs.arity!=1: raise FiniteError('an observation must be unary')
    out,labels = defaultdict(list),[]
    for x in carrier.elements:
        lab = obs(x)
        labels.append(lab)
        out[lab].append(x)
    _ensure_dict_keys(labels)
    return dict(out)

def kernel_pairs(carrier,obs):
    return [pair for members in fibers(carrier,obs).values() for pair in itertools.combinations(members,2)]

def related(obs,a,b): return value_key(obs(a))==value_key(obs(b))

@dataclass
class DescentHit:
    inputs_a: tuple
    inputs_b: tuple
    image_a: Any
    image_b: Any
    reason: str

def search_descent(carrier,eq_obs,op,*,external=False):
    """Evaluate every input; return representatives witnessing separation.

    Endomorphism outputs compare equivalence. External outputs compare equality.
    Certificates are not the count of all unordered colliding pairs.
    """
    obs = materialize(carrier,eq_obs)
    operation = materialize(carrier,op,closed=not external)
    representatives,hits = {},[]
    for args in input_tuples(carrier,op.arity):
        key = tuple(value_key(obs(x)) for x in args)
        output = operation(*args)
        label = value_key(output if external else obs(output))
        if key not in representatives: representatives[key] = (args,output,label)
        else:
            earlier,earlier_output,earlier_label = representatives[key]
            if label!=earlier_label:
                hits.append(DescentHit(earlier,args,earlier_output,output,
                    f'{earlier!r} ~ {args!r} but {op.name} outputs {earlier_output!r} and {output!r} separate'))
    return hits

def locus(carrier,pi,witness):
    if pi.arity!=1 or witness.arity!=1:
        raise FiniteError('locus requires unary retained and witness maps')
    w = materialize(carrier,witness)
    return {lab:splits for lab,members in fibers(carrier,pi).items()
            if (splits := [(a,b) for a,b in itertools.combinations(members,2) if not related(w,a,b)])}

def refinement_ok(carrier,finer,coarser):
    if finer.arity!=1 or coarser.arity!=1:
        raise FiniteError('refinement requires unary observations')
    fine,co = materialize(carrier,finer),materialize(carrier,coarser)
    representatives = {}
    for x in carrier.elements:
        key,label = value_key(fine(x)),value_key(co(x))
        if key in representatives:
            first,first_label = representatives[key]
            if label!=first_label:
                return False,(first,x)
        else:
            representatives[key] = (x,label)
    return True,None

def image_set(carrier,obs): return list(fibers(carrier,obs))
