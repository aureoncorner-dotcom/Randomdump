"""Exact circle-operator examples from the corrected v2.2 increment.

A_a=-i d/dtheta+a on periodic H^1(S^1), with spectrum Z+a.
The eta formula uses zeta(0,a)=1/2-a: https://dlmf.nist.gov/25.11.E13
No arbitrary operator or truncated-spectrum eta solver is claimed.
"""
from fractions import Fraction
from finite import FiniteError

def rational(value):
    if type(value) not in (int,str,Fraction): raise FiniteError('use an exact integer, rational string, or Fraction')
    try: return Fraction(value)
    except (ValueError,ZeroDivisionError) as e: raise FiniteError(f'invalid rational {value!r}') from e

def eta_circle(a):
    a = rational(a)
    if not 0<a<1: raise FiniteError('eta_circle uses the declared branch 0<a<1 without zero modes')
    return 1-2*a

def reduced_eta_circle(a):
    """Real reduced eta (eta+h)/2, with h=0; not reduction modulo integers."""
    return eta_circle(a)/2

def squared_spectrum_label(a):
    """Exact label for Spec(A_a^2) on 0<a<1 via a <-> 1-a reindexing."""
    a = rational(a)
    if not 0<a<1: raise FiniteError('squared-spectrum label uses 0<a<1')
    return min(a,1-a)

def endpoint_spectrum_label(a):
    a = rational(a)
    return a % 1

def affine_spectral_flow(start,end):
    """Signed crossings for the affine path A_((1-t)start+t*end).

    Invertible endpoints are required; upward crossings count positively.
    This helper is specific to this commuting affine circle family.
    """
    a,b = rational(start),rational(end)
    if a.denominator==1 or b.denominator==1: raise FiniteError('spectral-flow endpoints must be invertible')
    return b.numerator//b.denominator-a.numerator//a.denominator

def exact_examples():
    a,b = Fraction(1,4),Fraction(3,4)
    return {'E1':{'parameters':[a,b],'equal_squared_spectra':squared_spectrum_label(a)==squared_spectrum_label(b),
                  'eta':[eta_circle(a),eta_circle(b)],'reduced_eta_real':[reduced_eta_circle(a),reduced_eta_circle(b)],
                  'eta_separation':abs(eta_circle(a)-eta_circle(b)),
                  'reason':'bijection n -> -n-1 negates eigenvalues before squaring'},
            'E2':{'ordered_endpoint_spectral_labels':[[endpoint_spectrum_label('-1/2'),endpoint_spectrum_label('-1/2')],
                                                     [endpoint_spectrum_label('-1/2'),endpoint_spectrum_label('1/2')]],
                  'spectral_flow':[affine_spectral_flow('-1/2','-1/2'),affine_spectral_flow('-1/2','1/2')],
                  'reason':'constant path versus one upward n=0 crossing at t=1/2'},
            'scope':'the declared periodic circle operator and affine path examples only'}
