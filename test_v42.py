import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
BASELINE=ROOT.parent.parent/'outputs'
spec=importlib.util.spec_from_file_location('v42',ROOT/'DROP_IT_candidate.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

FAKE=r'''
import json,sys,re
from pathlib import Path
from math import isqrt
final,thread,scenario=sys.argv[1:]
name=Path(final).stem
prompt=sys.stdin.buffer.read().decode()
n=int(name[1:]) if name.startswith('S') else 0
thread=thread or ('primary' if n else name)
if scenario=='break' and n==3: thread='replacement'
print(json.dumps({'type':'thread.started','thread_id':thread}),flush=True)
print(json.dumps({'type':'turn.started'}),flush=True)
if scenario=='fail' and n==3:
    print(json.dumps({'type':'turn.failed','error':{'message':'synthetic failure'}}),flush=True)
    raise SystemExit(2)
if scenario=='compact' and n==3:
    print(json.dumps({'type':'context.compacted'}),flush=True)
    raise SystemExit(0)
if not n:
    reply=prompt.strip().splitlines()[-1]
else:
    reply=('Checking.\n' if n%3==0 else 'Hm. Right.\n' if n%7==0 else '')+'Here is the function.\n```python\ndef capture(raw): return raw\n```'
    prime=re.search(r'Use the prime n=(\d+)',prompt)
    if prime:
        p=int(prime[1])
        f=lambda a:0 if not a else (3*a-isqrt(5*a*a)-1)//2
        b=f(39*p)-39*f(p)
        bn=f(39*(p+1))-39*f(p+1)
        reply=f'{b}, {b%3}, {15-(bn-b)%39}\n'+reply
if n and n%5==0:
    print(json.dumps({'type':'item.completed','item':{'id':'i0','type':'agent_message','text':'Hmm.'}}),flush=True)
print(json.dumps({'type':'item.completed','item':{'id':'i1','type':'agent_message','text':reply}}),flush=True)
Path(final).write_bytes(reply.encode())
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':1,'output_tokens':1}}),flush=True)
'''


class Measurements(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='v42_test_',dir=ROOT)
        self.path=Path(self.temp.name).resolve()
        self.path.relative_to(ROOT)
        self.addCleanup(self.clean)

    def clean(self):
        self.path.resolve().relative_to(ROOT.resolve())
        for path in self.path.rglob('*'):
            if path.is_file(): path.chmod(0o666)
        self.temp.cleanup()

    def test_hash_gate_core_and_geometry(self):
        self.assertEqual(m.baseline_gate_v42(BASELINE)['hash_gate'],'PASS')
        report=m.geometry_gate_v42(BASELINE)
        self.assertEqual(report['states_compared'],10000)
        self.assertEqual(sum(report['field_mismatches'].values()),0)

    def test_plan_matches_baseline_and_carryover(self):
        plan=m.plan_v42((BASELINE/'task.txt').read_text())
        self.assertEqual(len(plan),64)
        self.assertEqual([row['condition'] for row in plan[:4]],list('CBDA'))
        self.assertEqual([plan[i]['prime'] for i in range(0,64,4)],[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53])
        self.assertEqual(plan[4]['geometry_exposures_before_n'],2)
        self.assertEqual(plan[4]['response_rule_exposures_before_n'],2)
        self.assertEqual(plan[4]['condition_prev1'],'A')
        self.assertEqual(plan[4]['geometry_clock'],{'from_n':3,'to_n':4})
        baseline=m.baseline_measurements_v42(BASELINE,m.codebook_v42(),plan)
        self.assertEqual(len(baseline['observations']),16)
        self.assertTrue(all(r['C_n_literal']==0 for r in baseline['observations']))
        self.assertTrue(all(any(i['is_final_message_item'] for i in t['items']) for t in baseline['event_topology']))

    def test_markers_burst_and_normalization(self):
        r=m.leading_markers_v42('Hmm. Right. Right. Mhm. Right. Hm. Huh. Right.\nDo the work.',m.codebook_v42())
        self.assertEqual(r['leading_marker_count_n'],8)
        self.assertEqual((r['W_n'],r['H_n'],r['A_n']),(0,1,1))
        r=m.leading_markers_v42('Hmmmmm. Uh. Ah. Okay.',m.codebook_v42())
        self.assertEqual(r['leading_marker_count_n'],4)
        self.assertFalse(r['segmentation'][0]['exact_match'])
        self.assertTrue(r['segmentation'][1]['standalone_item'])
        for text in ('One moment.','Let me take a beat.','Lemme take a quick look.','Pausing.','Checking the values.'):
            self.assertEqual(m.leading_markers_v42(text,m.codebook_v42())['W_n'],1,text)

    def test_quotes_code_metadata_not_marker(self):
        for text in ('```python\nChecking = 1\n```','> Checking.','"Checking."', '`Checking`','The Checking variable is zero.','Hmmography.','Rightfully done.'):
            r=m.leading_markers_v42(text,m.codebook_v42())
            self.assertEqual((r['W_n'],r['H_n'],r['A_n']),(0,0,0),text)
        body,header=m.split_math_header('29, 2, 0\nChecking.\nDone.',[29,2,0])
        self.assertTrue(m.preamble_markers(body)['checking_prefix'])
        self.assertFalse(m.preamble_markers('Hmm. Checking.')['checking_prefix'])

    def test_transition_denominators_and_structural_zeros(self):
        values=[0,0,1,0,1,1,1,0]
        records=[{'turn_index':i+1,'condition':'ABCD'[i%4],'C_n_literal':v,'C_prev1':values[i-1] if i else None,'C_prev2':values[i-2] if i>1 else None} for i,v in enumerate(values)]
        tr=m.transitions_v42(records)
        self.assertEqual(tr['first_order']['pooled']['counts'],[[1,2],[2,2]])
        self.assertEqual(tr['first_order']['pooled']['p11'],{'numerator':2,'denominator':4,'probability':.5})
        self.assertEqual(sum(map(sum,tr['second_order']['counts'])),6)
        zeros=[{'turn_index':i+1,'condition':'A','C_n_literal':0,'C_prev1':0 if i else None,'C_prev2':0 if i>1 else None} for i in range(4)]
        empty=m.transitions_v42(zeros)
        self.assertIsNone(empty['first_order']['pooled']['p11']['probability'])
        self.assertIsNone(empty['first_order']['pooled']['Lambda'])
        self.assertEqual(empty['second_order']['T2'][1],[0,0,None,None])
        self.assertEqual(empty['second_order']['T2'][0],[1,0,0,0])

    def test_run_structure(self):
        r=m.run_structure_v42([1,1,0,1,0,1,1,1])
        self.assertEqual((r['total_positives'],r['number_of_positive_runs'],r['maximum_positive_run_length'],r['adjacent_positive_positive_count']),(6,3,3,3))
        self.assertEqual(r['run_length_histogram'],{1:1,2:1,3:1})

    def test_context_detection_excludes_assistant_content(self):
        self.assertEqual(m.context_events_v42({'type':'item.completed','item':{'type':'agent_message','text':'history replaced'}},b'','stdout',1),[])
        self.assertEqual(len(m.context_events_v42({'type':'context.compacted'},b'','stdout',1)),1)

    def test_documented_arguments(self):
        c={'executable':'codex','model_requested':'gpt-6-astra','reasoning_mode':'max','service_tier':'priority'}
        first=m.arguments_v42(c,'PRIMARY_SEQUENCE',None,'reply')
        resume=m.arguments_v42(c,'PRIMARY_SEQUENCE','thread-1','reply')
        self.assertNotIn('--ephemeral',first)
        self.assertNotIn('--ephemeral',resume)
        self.assertEqual(resume[-2:],['thread-1','-'])
        self.assertEqual(resume[1:5],['exec','--sandbox','read-only','resume'])

    def exercise(self,scenario):
        out=self.path/scenario
        fake=self.path/(scenario+'.py')
        fake.write_text(FAKE,encoding='utf-8')
        def fake_runtime(c):
            return {'executable_sha256':c['executable_sha256'],'state_database_path':None,'state_database_accessible':None,'fixture':True}
        def fake_args(c,role,resume,final):
            return [sys.executable,str(fake),str(final),resume or '',scenario]
        with patch.object(m,'runtime_v42',fake_runtime),patch.object(m,'arguments_v42',fake_args),redirect_stdout(io.StringIO()):
            m.prepare_v42(out,BASELINE,ROOT)
            code=m.run_sequence_v42(out)
        status=json.loads((out/'COHORT_STATUS.json').read_bytes())
        report=json.loads((out/'SEQUENTIAL_TRIAL_REPORT.json').read_bytes())
        return code,status,report,out

    def test_complete_synthetic_pipeline(self):
        code,status,report,out=self.exercise('normal')
        self.assertEqual((code,status['status'],status['completed']),(0,'COMPLETED',64))
        self.assertEqual(report['OBSERVED']['invocation_count'],66)
        self.assertEqual(report['DERIVED']['comparisons']['FULL_64']['rates']['C_n_literal']['numerator'],21)
        self.assertEqual(report['DERIVED']['comparisons']['FULL_64']['rates']['U_n']['numerator'],12)
        self.assertEqual(report['DERIVED']['geometry_answers']['correct'],32)
        self.assertEqual(report['OBSERVED']['distinct_primary_thread_ids'],['primary'])
        validation=json.loads((out/'PACKAGE_VALIDATION_v42.json').read_bytes())
        self.assertEqual(validation['member_hash_errors'],0)
        with self.assertRaisesRegex(ValueError,'sequence_already_started'):
            m.run_sequence_v42(out)

    def test_broken_thread_no_retry_and_no_post(self):
        code,status,report,out=self.exercise('break')
        self.assertEqual((code,status['status'],status['completed']),(3,'HALTED',2))
        self.assertEqual(report['OBSERVED']['primary_invocation_count'],3)
        self.assertEqual(json.loads((out/'CANARY_POST_REPORT.json').read_bytes())['status'],'NOT_RUN_HALT')

    def test_failed_turn_no_retry(self):
        code,status,report,out=self.exercise('fail')
        self.assertEqual((code,status['completed']),(3,2))
        self.assertEqual(report['OBSERVED']['primary_invocation_count'],3)

    def test_compaction_halts(self):
        code,status,report,out=self.exercise('compact')
        self.assertEqual((code,status['completed']),(3,2))
        self.assertIn('context.compacted',status['failure']['observed_literal'])


if __name__=='__main__':
    unittest.main(verbosity=2)
