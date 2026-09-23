import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import compiler
from finite import Carrier,EvalMap,FiniteError,search_descent,locus,refinement_ok,compile_expr
from calculus import joint,next_output,factor,minimal_attachments,autonomous_refinement,MarkovKernel,representation_gap
from geometry import Partition,compare,join,svg_atlas
from spectral import eta_circle,exact_examples,affine_spectral_flow,squared_spectrum_label
from toroidal import reference_cycles,divergence,cut_fluxes,signed_winding,modular_flux

COUNTS = {'unary_descent':0,'binary_descent':0,'refinement':0,'locus':0,'locus_product':0,'restriction':0,'witness_coarsening':0,'observation_refinement':0,'autonomous_refinement_models':0,'toroidal_fixtures':0}

def partitions(n):
    def rec(prefix):
        if len(prefix)==n: yield tuple(prefix)
        else:
            for x in range(max(prefix,default=-1)+2): yield from rec(prefix+[x])
    return rec([])

def em(values,name='obs'):
    return EvalMap(name,table=dict(enumerate(values)))

def base():
    return 'category Set\nsource P\ncarrier P { elements 0 1 }\nwitness W on P {\n observation Omega : P -> Y\n eval x |-> x\n}\nequivalence R := kernel_pair(Omega)\nquotient Q := P / R\n'

class CompilerRegression(unittest.TestCase):
    def test_original_examples(self):
        rejects = {'bad_algker_in_set','finite_bad_pair','finite_incomparable','finite_refine_reversed','top_iso_blocked'}
        findings = {'finite_floor_fail','finite_locus_sector','finite_service','parity_floor_fail','service_compliance','toroidal_sector'}
        for path in sorted((ROOT/'examples').glob('*.gqg')):
            if path.stem.startswith('new_'): continue
            with self.subTest(file=path.name):
                _,report = compiler.compile_source(path.read_text(encoding='utf-8'))
                expected = 'REJECT' if path.stem in rejects else 'FINDING' if path.stem in findings else 'ACCEPT'
                self.assertIn(expected,report.splitlines()[0])

    def test_previous_review_cases(self):
        valid = {'binary_table_json','mixed_table_json','mixed_carrier_binary_comparison','vect_non_linear_iso'}
        for path in sorted((ROOT/'tests'/'cases').glob('*.gqg')):
            with self.subTest(file=path.name):
                try:
                    p,report = compiler.compile_source(path.read_text(encoding='utf-8'))
                    verdict = report.splitlines()[0].split()[-2]
                except (compiler.ParseError,FiniteError): verdict='REJECT'
                expected = 'FINDING' if path.stem=='multiple_loci_overwrite' else 'ACCEPT' if path.stem in valid else 'REJECT'
                self.assertEqual(verdict,expected)

    def test_missing_certificate_exit_and_batch_continuation(self):
        result = subprocess.run([sys.executable,'-B',str(ROOT/'compiler.py'),'--json',
                    str(ROOT/'tests/cases/invalid_formula_syntax.gqg'),
                    str(ROOT/'tests/cases/missing_descent_certificate.gqg'),
                    str(ROOT/'examples/finite_parity_add.gqg')],capture_output=True,text=True,encoding='utf-8',timeout=20)
        self.assertEqual(result.returncode,1)
        rows = [json.loads(x) for x in result.stdout.splitlines()]
        self.assertEqual([r['verdict'] for r in rows],['REJECT','REJECT','ACCEPT'])
        self.assertNotIn('Traceback',result.stderr)

    def test_hash_stable_across_check(self):
        for name in ('finite_parity_add.gqg','finite_service.gqg'):
            p = compiler.parse((ROOT/'examples'/name).read_text(encoding='utf-8'))
            first = compiler.ast_hash(p)
            compiler.check(p)
            self.assertEqual(first,compiler.ast_hash(p))
            report = compiler.report(p)
            compiler.check(p)
            self.assertEqual(report,compiler.report(p))

    def test_typed_json_keys_and_order(self):
        p = compiler.parse((ROOT/'tests/cases/binary_table_json.gqg').read_text())
        q = compiler.parse((ROOT/'tests/cases/binary_table_json.gqg').read_text())
        q.by_kind('OP')[0].payload['table'] = dict(reversed(list(q.by_kind('OP')[0].payload['table'].items())))
        self.assertEqual(compiler.ast_hash(p),compiler.ast_hash(q))
        self.assertNotEqual(compiler.json_value({1:'a'}),compiler.json_value({'1':'a'}))
        self.assertNotEqual(compiler.json_value({(1,2):'a'}),compiler.json_value({'(1,2)':'a'}))

    def test_formula_restrictions(self):
        for formula in ('__import__("os")','x.__class__','[x for x in (1,2)]','abs(x, ignored=1)','x // 0','x +', '"x" * 1000000000'):
            with self.subTest(formula=formula),self.assertRaises(FiniteError): compile_expr(formula)({'x':1})
        self.assertEqual(compile_expr('rat(1,2) if x < 2 else rat(-1,2)')({'x':1}),F(1,2))
        self.assertEqual(compile_expr('0 <= x < 3')({'x':2}),True)

    def test_singletons_and_carrier_aliases(self):
        with self.assertRaises(FiniteError): Carrier('P',[0,False])
        with self.assertRaises(FiniteError): Carrier('P',[0,0])
        with self.assertRaises(FiniteError): search_descent(Carrier('P',[0,1]),em([0,1]),EvalMap('f',table={0:0}))

    def test_parser_duplicates_and_inline(self):
        p,report = compiler.compile_source(base())
        self.assertIn('ACCEPT',report)
        bad = base()+'operation f : P -> P {\n0 -> 0\n0 -> 1\n}\n'
        with self.assertRaises(compiler.ParseError): compiler.parse(bad)
        _,report = compiler.compile_source(base()+'equivalence R := kernel_pair(Omega)\n')
        self.assertIn('REJECT',report)
        with self.assertRaises(compiler.ParseError):
            compiler.parse('category Set\nsource P\nwitness W on P {\nobservation A : P -> Y\nobservation B : P -> Y\n}\n')

    def test_quoted_comment_marker(self):
        source = base().replace('eval x |-> x','eval x |-> "#{}"')
        p,_ = compiler.compile_source(source)
        self.assertEqual(p.by_kind('OBS')[0].payload['fibers'][0]['label'],'#{}')

    def test_derived_cycles_rejected(self):
        _,report = compiler.compile_source(base()+'joint A := B Omega\njoint B := A Omega\n')
        self.assertIn('REJECT',report)

    def test_formulas_checked_without_carrier(self):
        _,report = compiler.compile_source('category Set\nsource P\noperation bad : P -> P { eval x |-> x + }\n')
        self.assertIn('REJECT',report)

    def test_unary_witness_required_on_singleton_fibers(self):
        car = Carrier('P',[0,1])
        identity = em([0,1])
        binary = EvalMap('binary',['x','y'],formula='x')
        with self.assertRaises(FiniteError): locus(car,identity,binary)
        with self.assertRaises(FiniteError): refinement_ok(car,identity,binary)

class GeometryTests(unittest.TestCase):
    def test_all_split_witnesses_survive_svg(self):
        p,_ = compiler.compile_source((ROOT/'tests/cases/multiple_loci_overwrite.gqg').read_text())
        root = ET.fromstring(p.geometry_svg)
        labels = [x.text for x in root.iter('{http://www.w3.org/2000/svg}text')]
        self.assertIn('SPLIT 0',labels); self.assertIn('SPLIT 1',labels)
        self.assertIn('by OA',labels); self.assertIn('by OB',labels)

    def test_unequal_carriers_rejected(self):
        with self.assertRaises(FiniteError): compare(Partition('A',{0:[1]}),Partition('B',{0:[2]}))

    def test_mixed_elements_comparison(self):
        fine = Partition('F',{0:[0],1:['alpha']})
        coarse = Partition('C',{0:['alpha',0]})
        self.assertEqual(compare(fine,coarse),'finer')
        self.assertEqual(sum(map(len,join(fine,coarse,'J').fibers.values())),2)

    def test_svg_wraps_and_escapes(self):
        p = Partition('long name <&>'+('x'*200),{'<tag>':['verylong_'+('z'*150),*range(40)]})
        svg = svg_atlas([p],title='<title>&"')
        root = ET.fromstring(svg)
        self.assertEqual(root.find('{http://www.w3.org/2000/svg}title').text,'<title>&"')
        height = float(root.attrib['height'])
        for text in root.iter('{http://www.w3.org/2000/svg}text'):
            self.assertLess(float(text.attrib['y']),height)
            self.assertLessEqual(len(text.text or ''),120)

class ExhaustiveFinite(unittest.TestCase):
    def test_all_small_autonomous_refinements(self):
        for n in range(1,4):
            car = Carrier('P',list(range(n)))
            parts = list(partitions(n))
            for b in parts:
                for targets in itertools.product(range(n),repeat=n):
                    output,update = em(b),em(targets)
                    q = autonomous_refinement(car,output,update)['partition']
                    self.assertFalse(search_descent(car,q,update))
                    self.assertTrue(refinement_ok(car,q,output)[0])
                    for candidate in parts:
                        cand = em(candidate)
                        if refinement_ok(car,cand,output)[0] and not search_descent(car,cand,update):
                            self.assertTrue(refinement_ok(car,cand,q)[0])
                    COUNTS['autonomous_refinement_models'] += 1

    def test_coarsening_and_refining_loci(self):
        car = Carrier('P',[0,1,2])
        for pi,wfine,wcoarse in itertools.product(list(partitions(3)),repeat=3):
            if refinement_ok(car,em(wfine),em(wcoarse))[0]:
                self.assertLessEqual(set(locus(car,em(pi),em(wcoarse))),set(locus(car,em(pi),em(wfine))))
                COUNTS['witness_coarsening'] += 1
            if refinement_ok(car,em(wfine),em(pi))[0]:
                fine_locus = locus(car,em(wfine),em(wcoarse))
                mapped = {pi[x] for x in range(3) if wfine[x] in fine_locus}
                self.assertLessEqual(mapped,set(locus(car,em(pi),em(wcoarse))))
                COUNTS['observation_refinement'] += 1
    def test_small_exact_models(self):
        for n in range(1,5):
            states = tuple(range(n)); car = Carrier('P',list(states)); parts = list(partitions(n))
            for p in parts:
                obs = em(p)
                for outputs in itertools.product(states,repeat=n):
                    expected = any(p[a]==p[b] and p[outputs[a]]!=p[outputs[b]] for a in states for b in states)
                    self.assertEqual(bool(search_descent(car,obs,em(outputs,'f'))),expected)
                    COUNTS['unary_descent'] += 1
                for q in parts:
                    expected = all(p[a]!=p[b] or q[a]==q[b] for a in states for b in states)
                    self.assertEqual(refinement_ok(car,obs,em(q))[0],expected); COUNTS['refinement'] += 1
                    labels = {p[a] for a in states for b in states if p[a]==p[b] and q[a]!=q[b]}
                    self.assertEqual(set(locus(car,obs,em(q))),labels); COUNTS['locus'] += 1
            if n<=2:
                tuples = list(itertools.product(states,repeat=2))
                for p in parts:
                    for outputs in itertools.product(states,repeat=n*n):
                        expected = any(p[a[0]]==p[b[0]] and p[a[1]]==p[b[1]] and p[outputs[i]]!=p[outputs[j]] for i,a in enumerate(tuples) for j,b in enumerate(tuples))
                        op = EvalMap('add',['x','y'],table=dict(zip(tuples,outputs)))
                        self.assertEqual(bool(search_descent(car,em(p),op)),expected); COUNTS['binary_descent'] += 1

    def test_product_and_restriction_calculus(self):
        car = Carrier('P',[0,1,2])
        parts = list(partitions(3))
        for p,a,b in itertools.product(parts,repeat=3):
            pi,wa,wb = em(p),em(a),em(b)
            self.assertEqual(set(locus(car,pi,joint(car,wa,wb))),set(locus(car,pi,wa))|set(locus(car,pi,wb)))
            COUNTS['locus_product'] += 1
        for p,w in itertools.product(parts,repeat=2):
            for size in (1,2,3):
                for subset in itertools.combinations(range(3),size):
                    restricted = Carrier('C',list(subset))
                    self.assertLessEqual(set(locus(restricted,em(p),em(w))),set(locus(car,em(p),em(w))))
                    COUNTS['restriction'] += 1

class UpdatedCalculus(unittest.TestCase):
    def setUp(self): self.car = Carrier('P',[0,1,2,3])

    def test_current_vs_next_output(self):
        b,u = em([0,0,1,1],'B'),em([2,0,2,3],'U')
        self.assertFalse(factor(self.car,b,b)['counterexamples'])
        self.assertTrue(factor(self.car,b,next_output(self.car,b,u))['counterexamples'])
        stable = autonomous_refinement(self.car,b,u)
        self.assertFalse(stable['transition']['counterexamples'])
        self.assertFalse(stable['output']['counterexamples'])
        self.assertEqual(len(set(stable['partition'](x) for x in self.car.elements)),3)

    def test_inclusion_minimal_not_only_fewest(self):
        menu = {'bit0':em([0,1,0,1]),'bit1':em([0,0,1,1]),'identity':em([0,1,2,3])}
        repairs = minimal_attachments(self.car,em([0]*4),em([0,1,2,3]),menu)
        self.assertEqual(set(repairs),{('identity',),('bit0','bit1')})

    def test_residual_pair_dynamics(self):
        car = Carrier('state_pairs',list(itertools.product(range(3),repeat=2)))
        residual = EvalMap('delta',_fn=lambda p:p[1]-p[0])
        lift = EvalMap('lift',_fn=lambda p:(p[1],(p[1]*p[1])%3))
        self.assertTrue(factor(car,residual,next_output(car,residual,lift))['counterexamples'])

    def test_representation_gap(self):
        result = representation_gap(self.car,em([0,1,2,3]),[2,4])
        self.assertTrue(result['injective_on_carrier']); self.assertEqual(result['missing_objects'],[4])

    def test_exact_stochastic_laws_and_loss(self):
        car = Carrier('P',[0,1,2])
        kernel = MarkovKernel(car,{0:{0:'1/2',2:'1/2'},1:{1:'1/4',2:'3/4'},2:{2:1}})
        pi = em([0,0,1])
        self.assertEqual(kernel.strong_lumpability(pi)['status'],'counterexample')
        prior = F(0)
        for h in (1,2,3):
            loss = kernel.horizon_diameters(pi,pi,h)['fibers'][0]['diameter']
            self.assertGreaterEqual(loss,prior); prior = loss
            for law in kernel.future_laws(pi,h).values(): self.assertEqual(sum(law.values()),1)
        self.assertEqual(kernel.horizon_diameters(pi,pi,1)['fibers'][0]['diameter'],F(1,4))
        self.assertEqual(kernel.strong_lumpability(em([0,0,0]))['status'],'tested_only')
        self.assertEqual(kernel.horizon_diameters(em([0,1,2]),pi,3)['fibers'][0]['diameter'],0)

    def test_kernel_rejects_bad_probabilities(self):
        for rows in ({0:{0:0.5,1:0.5},1:{1:1}},{0:{0:'1/3'},1:{1:1}},{0:{2:1},1:{1:1}}):
            with self.assertRaises(FiniteError): MarkovKernel(Carrier('P',[0,1]),rows)

    def test_horizon_uses_joint_histories(self):
        car = Carrier('P',[0,1,2,3])
        kernel = MarkovKernel(car,{0:{2:1},1:{3:1},2:{2:1},3:{2:1}})
        retained,output = em([0,0,1,2]),em([0,0,1,0])
        self.assertEqual(kernel.horizon_diameters(retained,output,1)['fibers'][0]['diameter'],1)
        self.assertEqual(kernel.horizon_diameters(retained,output,2)['fibers'][0]['diameter'],1)
        # The second-time marginal agrees, although the full two-output laws differ.
        law = kernel.future_laws(output,2)
        self.assertEqual({history[-1] for history in law[0]},{history[-1] for history in law[1]})

    def test_spectral_exact_family(self):
        examples = exact_examples()
        self.assertEqual(examples['E1']['eta'],[F(1,2),F(-1,2)])
        self.assertEqual(examples['E2']['spectral_flow'],[0,1])
        for n in range(-100,101): self.assertEqual((F(n)+F(3,4))**2,(F(-n-1)+F(1,4))**2)
        self.assertEqual(squared_spectrum_label('1/4'),squared_spectrum_label('3/4'))
        self.assertEqual(affine_spectral_flow('1/2','-1/2'),-1)
        with self.assertRaises(FiniteError): eta_circle(0)
        with self.assertRaises(FiniteError): affine_spectral_flow(0,'1/2')

    def test_signed_toroidal_fixtures(self):
        for size in (2,3):
            shape = (size,)*3
            for q in itertools.product(range(2),repeat=3):
                for offsets in itertools.product((-1,0,1),repeat=3):
                    winding = tuple(a+2*b for a,b in zip(q,offsets))
                    current = reference_cycles(shape,winding)
                    self.assertFalse(any(divergence(shape,current).values()))
                    self.assertEqual(signed_winding(shape,current),winding)
                    self.assertEqual(tuple(w%2 for w in signed_winding(shape,current)),q)
                    self.assertEqual(modular_flux(shape,current),tuple(w%6 for w in winding))
                    COUNTS['toroidal_fixtures'] += 1
        sourced = {((0,0,0),0):6}
        with self.assertRaises(FiniteError): signed_winding((2,2,2),sourced)
        self.assertEqual(modular_flux((2,2,2),sourced),(0,0,0))

if __name__=='__main__': unittest.main()
