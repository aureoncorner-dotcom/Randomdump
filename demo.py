"""Generate examples, diagrams, and exact result data in out/."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sys
import compiler
from finite import Carrier,EvalMap
from calculus import factor,joint,next_output,autonomous_refinement,minimal_attachments,MarkovKernel,representation_gap
from spectral import exact_examples
from toroidal import reference_cycles,signed_winding
from geometry import from_fiber_dict,svg_atlas
from finite import fibers

def run():
    root = Path(__file__).resolve().parent
    out = root/'out'
    out.mkdir(exist_ok=True)
    results = {'compiler':{}}
    for name in ('new_prediction','new_spectral_eta','new_spectral_flow'):
        program,report = compiler.compile_source((root/'examples'/f'{name}.gqg').read_text(encoding='utf-8'))
        (out/f'{name}.txt').write_text(report,encoding='utf-8')
        (out/f'{name}.svg').write_text(program.geometry_svg,encoding='utf-8')
        results['compiler'][name] = report.splitlines()[0]
    car = Carrier('P',[0,1,2,3])
    retained = EvalMap('current',table={0:0,1:0,2:1,3:1})
    update = EvalMap('update',table={0:2,1:0,2:2,3:3})
    stable = autonomous_refinement(car,retained,update)
    results['autonomous_refinement'] = {'classes':fibers(car,stable['partition']),
                                      'transition':stable['transition'],'rounds':stable['rounds']}
    identity = EvalMap('identity',table={x:x for x in car.elements})
    menu = {'bit0':EvalMap('bit0',formula='x % 2'),'bit1':retained,'identity':identity}
    results['minimal_attachments'] = minimal_attachments(car,EvalMap('constant',formula='0'),identity,menu)
    result_parts = [from_fiber_dict('current',fibers(car,retained)),from_fiber_dict('autonomous',fibers(car,stable['partition']))]
    (out/'autonomous_refinement.svg').write_text(svg_atlas(result_parts,title='Current output and finite autonomous refinement',refinements=[('autonomous','current')]),encoding='utf-8')
    pairs = Carrier('state_pairs',list(product(range(3),repeat=2)))
    residual = EvalMap('delta',_fn=lambda p:p[1]-p[0])
    lift = EvalMap('pair_update',_fn=lambda p:(p[1],(p[1]*p[1])%3))
    results['residual_closure'] = factor(pairs,residual,next_output(pairs,residual,lift))
    stochastic_car = Carrier('finite_model',[0,1,2])
    kernel = MarkovKernel(stochastic_car,{0:{0:'1/2',2:'1/2'},1:{1:'1/4',2:'3/4'},2:{2:1}})
    pi = EvalMap('retained',table={0:0,1:0,2:1})
    results['strong_lumpability'] = kernel.strong_lumpability(pi)
    results['finite_horizon_loss'] = [kernel.horizon_diameters(pi,pi,h) for h in (1,2,3)]
    results['spectral'] = exact_examples()
    results['representation_gap'] = representation_gap(car,identity,[2,4])
    results['toroidal_signed_fixture'] = signed_winding((3,3,3),reference_cycles((3,3,3),(-1,2,3)))
    results['scope'] = 'declared finite models and the stated exact spectral family; no empirical replay or toroidal all-orders proof'
    (out/'demo_results.json').write_text(json.dumps(compiler.json_value(results),ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Created diagrams, reports, and demo_results.json in {out}')
    return results

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    run()
