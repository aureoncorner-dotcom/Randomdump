"""CC0-1.0 new code. Controlled correction application; no model inference.
Original and changed clues retain seven distinct objects. Source labels are
transported through a declared renaming, independently of the decision solver.
"""
import copy,hashlib,json,re
from pathlib import Path
import ordering_solver as solver

ROOT=Path(__file__).resolve().parent

def digest(s):return hashlib.sha256(s.encode()).hexdigest()

def answer(question):
    result=solver.solve(solver.parse(question))
    if len(result['entailed'])!=1:return {'answer':None,'reference_hash':digest(question)}
    return {'answer':result['entailed'][0],'reference_hash':digest(question)}

def correction(question,identity):
    parsed=solver.parse(question);names=parsed['names']
    rename={name:names[(i+(0 if identity else 1))%7] for i,name in enumerate(names)}
    context,options=question.split('\nOptions:\n')
    intro,tail=context.split(': ',1);roster,clues=tail.split('. ',1)
    pattern=re.compile(r'(?<!\w)(?:'+'|'.join(re.escape(n) for n in sorted(names,key=len,reverse=True))+r')(?!\w)')
    changed=intro+': '+roster+'. '+pattern.sub(lambda m:rename[m[0]],clues)+'\nOptions:\n'+options
    # Check syntax translation against the intended symbolic transformation.
    actual=solver.parse(changed)
    expected_clues=[]
    for kind,a,b in parsed['clues']:
        expected_clues.append([kind,rename[a],rename[b] if kind=='before' else b])
    if actual['clues']!=expected_clues or actual['options']!=parsed['options']:
        raise ValueError('Correction failed to preserve its declared meaning')
    return changed,rename,parsed

def transported_target(original_target,parsed,rename):
    kind,name,rank=parsed['options'][original_target]
    if kind!='at':raise ValueError('Unsupported target transport')
    transformed=[kind,rename[name],rank]
    matches=[k for k,v in parsed['options'].items() if v==transformed]
    if len(matches)!=1:raise ValueError('Target transport not unique')
    return matches[0]

def run():
    source=ROOT/'source/tasks.json'
    manifest=json.loads((ROOT/'source_manifest.json').read_text())
    item=next(f for f in manifest['files'] if f['local']=='tasks.json')
    if hashlib.sha256(source.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Source hash mismatch')
    tasks=json.loads(source.read_text())['examples']
    if len(tasks)!=250:raise ValueError('Unexpected corpus')
    rows=[]
    for i,t in enumerate(tasks):
        original=t['input'];prior=answer(original)
        if prior['answer']!=t['target'][1]:raise ValueError('Original solver/source disagreement')
        for identity in [True,False]:
            updated,rename,parsed=correction(original,identity)
            gold=transported_target(t['target'][1],parsed,rename)
            for arm in ['apply_before_answer','acknowledge_only','repair_after_acknowledgment']:
                # All arms start with the same prior answer and receive the same correction.
                # The first and third both perform substantive recomputation.
                events=['prior_answer_available','correction_received']
                if arm=='apply_before_answer':
                    events+=['active_reference_updated','recomputed','acknowledged']
                    final=answer(updated)
                elif arm=='acknowledge_only':
                    events+=['acknowledged','prior_answer_retained']
                    final=copy.deepcopy(prior)
                else:
                    events+=['acknowledged','active_reference_updated','recomputed']
                    final=answer(updated)
                rows.append({'task_id':i,'condition':'identity_control' if identity else 'changed_clues',
                  'arm':arm,'events':events,'acknowledged':True,'original_question':original,
                  'corrected_question':updated,'rename':rename,'prior':prior,'final':final,
                  'expected_transported_target':gold,'active_reference_hash':digest(updated),
                  'reference_current':final['reference_hash']==digest(updated),
                  'answer_correct':final['answer']==gold})
    results=ROOT/'results';results.mkdir(exist_ok=True)
    path=results/'receipts.jsonl'
    path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    reread=[json.loads(s) for s in path.read_text().splitlines()]
    for r in reread:
        if r['active_reference_hash']!=digest(r['corrected_question']):raise ValueError('Serialization mismatch')
    summary={'kind':'CONTROLLED_SOFTWARE_TEST','fresh_model_calls':0,'source_tasks':250,
      'pipeline_evaluations':len(rows),'conditions':{}}
    for cond in ['identity_control','changed_clues']:
        summary['conditions'][cond]={}
        for arm in ['apply_before_answer','acknowledge_only','repair_after_acknowledgment']:
            rr=[r for r in rows if r['condition']==cond and r['arm']==arm]
            summary['conditions'][cond][arm]={'cases':len(rr),'acknowledged':sum(r['acknowledged'] for r in rr),
                'correct':sum(r['answer_correct'] for r in rr),'current_reference':sum(r['reference_current'] for r in rr)}
    # A coarse report keeps acknowledgment only. An explicit pair is a witness
    # that this report is insufficient to reconstruct substantive correction.
    pair=[next(r for r in rows if r['task_id']==0 and r['condition']=='changed_clues' and r['arm']==a)
          for a in ['apply_before_answer','acknowledge_only']]
    witness={'projection':'acknowledged','witness':'answer_correct',
             'records':[{'task_id':r['task_id'],'arm':r['arm'],'projection':r['acknowledged'],
                         'witness':r['answer_correct'],'answer':r['final']['answer'],
                         'expected':r['expected_transported_target']} for r in pair],
             'equal_projection':pair[0]['acknowledged']==pair[1]['acknowledged'],
             'different_witness':pair[0]['answer_correct']!=pair[1]['answer_correct']}
    (results/'projection_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    summary['projection_counterexample']=witness['equal_projection'] and witness['different_witness']
    summary['design_limits']=['Clue changes are engineered to move the correct answer in every changed case.',
      'The program implements the interventions explicitly; this is not an estimate of model behavior.',
      'Late substantive repair and early substantive correction use the same solver.',
      'Source questions share constraint paragraphs; cases are not independent population samples.',
      'No language comparison, runtime-internal observation, or physical mechanism is tested.']
    (results/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':run()
