"""CC0-1.0 (new code only). Exhaustive replay of published BBH ordering responses.
Source data and historical responses retain their source license.
No model API calls. No targets enter parse/solve/decide.
"""
import argparse
import hashlib
import itertools
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def require(ok,msg):
    if not ok: raise ValueError(msg)

def clause(s,names):
    for name in sorted(names,key=len,reverse=True):
        for prefix in [name+' finished ', 'The '+name+' is ', 'The '+name+' are ']:
            if not s.startswith(prefix): continue
            rest=s[len(prefix):]
            directions={'above ':True,'below ':False,'newer than the ':True,'older than the ':False,
                        'to the left of the ':True,'to the right of the ':False,
                        'more expensive than the ':True,'less expensive than the ':False}
            for key,forward in directions.items():
                if rest.startswith(key):
                    other=rest[len(key):]
                    require(other in names,'Unknown object: '+s)
                    return ['before',name,other] if forward else ['before',other,name]
            ranks={'first':0,'second':1,'third':2,'fourth':3,'third-to-last':4,'second-to-last':5,'last':6,
                   'the leftmost':0,'the second from the left':1,'the third from the left':2,
                   'the fourth from the left':3,'the third from the right':4,'the second from the right':5,'the rightmost':6,
                   'the newest':0,'the second-newest':1,'the third-newest':2,'the fourth-newest':3,
                   'the third-oldest':4,'the second-oldest':5,'the oldest':6,
                   'the most expensive':0,'the second-most expensive':1,'the third-most expensive':2,
                   'the fourth-most expensive':3,'the third-cheapest':4,'the second-cheapest':5,'the cheapest':6}
            if rest in ranks:return ['at',name,ranks[rest]]
    raise ValueError('Unrecognized clause: '+s)

def parse(text):
    context,choices=text.split('\nOptions:\n')
    tail=context.split(': ',1)[1]
    roster,clues=tail.split('. ',1)
    names=[re.sub(r'^(a|an) ','',x) for x in roster.replace(', and ', ', ').split(', ')]
    require(len(names)==len(set(names))==7,'Invalid roster')
    statements=clues.rstrip('.').split('. ')
    require(bool(statements),'Missing clues')
    rules=[clause(s,names) for s in statements]
    options={}
    for line in choices.splitlines():
        m=re.fullmatch(r'\(([A-G])\) (.+)',line)
        require(m is not None,'Invalid option syntax')
        options[m[1]]=clause(m[2],names)
    require(set(options)==set('ABCDEFG'),'Missing option')
    return {'names':names,'clues':rules,'options':options,'original_clauses':statements}

def holds(rule,positions):
    kind,a,b=rule
    return positions[a]<positions[b] if kind=='before' else positions[a]==b

def solve(problem):
    valid=[]
    for order in itertools.permutations(problem['names']):
        positions={name:i for i,name in enumerate(order)}
        if all(holds(c,positions) for c in problem['clues']):valid.append(order)
    if not valid:return {'entailed':[],'valid_orders':[],'reason':'inconsistent constraints'}
    entailed=[letter for letter,c in problem['options'].items()
              if all(holds(c,{name:i for i,name in enumerate(o)}) for o in valid)]
    return {'entailed':entailed,'valid_orders':valid,'reason':None}

def decide(question,prediction):
    problem=parse(question)
    result=solve(problem)
    m=re.fullmatch(r'\(([A-G])\)',prediction.strip())
    candidate=m[1] if m else None
    chosen=result['entailed'][0] if len(result['entailed'])==1 else None
    accepted=chosen is not None and candidate==chosen
    status='ACCEPT_PRIMARY' if accepted else ('RECOVERED' if chosen else 'UNRESOLVED')
    counterexample=None
    if candidate and not accepted:
        for o in result['valid_orders']:
            if not holds(problem['options'][candidate],{name:i for i,name in enumerate(o)}):
                counterexample=o;break
    return {'parsed':problem,'candidate':candidate,'status':status,'final':chosen,
            'raw_counterexample':counterexample,**result}

def run(out):
    manifest=json.loads((ROOT/'source_manifest.json').read_text())
    for item in manifest['files']:
        require(hashlib.sha256((ROOT/'source'/item['local']).read_bytes()).hexdigest()==item['sha256'], 'Source hash mismatch')
    tasks=json.loads((ROOT/'source/tasks.json').read_text())['examples']
    responses=json.loads((ROOT/'source/model_outputs.json').read_text())['outputs']
    require(len(tasks)==len(responses)==250,'Unexpected corpus size')
    receipts=[]
    for i,(task,response) in enumerate(zip(tasks,responses)):
        question=response['input'].rsplit('\nQ: ',1)[1].removesuffix('\nA:')
        require(question==task['input'],'Question identity mismatch '+str(i))
        try: result=decide(question,response['prediction'])
        except (ValueError,KeyError,IndexError) as e:
            result={'status':'UNRESOLVED','final':None,'candidate':None,'error':str(e),'valid_orders':[],'entailed':[]}
        # Source labels are used only after the decision is complete.
        require(response['target']==task['target'],'Published target mismatch '+str(i))
        gold=task['target'][1]
        raw_match=re.fullmatch(r'\(([A-G])\)',response['prediction'].strip())
        raw_letter=raw_match[1] if raw_match else None
        receipts.append({'id':i,'question_sha256':hashlib.sha256(question.encode()).hexdigest(),
                         'prediction':response['prediction'],'published_target':gold,
                         'raw_wrong':raw_letter!=gold,
                         'solver_matches_target':result['final']==gold,
                         'wrong_accepted':result['final'] is not None and result['final']!=gold,**result})
    out.mkdir(exist_ok=True,parents=True)
    path=out/'receipts.json';path.write_text(json.dumps(receipts,indent=2)+'\n')
    saved=json.loads(path.read_text())
    require(len(saved)==250,'Serialized records missing')
    for row in saved:
        if row['final']:
            p=row['parsed'];models=row['valid_orders']
            require(bool(models),'Vacuous certificate')
            require(len(models)==len({tuple(x) for x in models}),'Duplicate models')
            for o in models:
                require(sorted(o)==sorted(p['names']),'Invalid permutation')
                pos={n:i for i,n in enumerate(o)}
                require(all(holds(c,pos) for c in p['clues']),'Invalid satisfying order')
                require(holds(p['options'][row['final']],pos),'Final option false in a retained order')
    summary={'corpus':'BBH logical_deduction_seven_objects','responses':'published code-davinci-002 direct few-shot outputs',
      'historical_replay':True,'new_model_calls':0,'injected_faults':0,'tasks':250,
      'raw_correct':sum(not r['raw_wrong'] for r in receipts),'raw_wrong':sum(r['raw_wrong'] for r in receipts),
      'accepted_primary':sum(r['status']=='ACCEPT_PRIMARY' for r in receipts),
      'recovered':sum(r['status']=='RECOVERED' for r in receipts),
      'unresolved':sum(r['status']=='UNRESOLVED' for r in receipts),
      'final_correct':sum(r['solver_matches_target'] for r in receipts),
      'wrong_accepted':sum(r['wrong_accepted'] for r in receipts),
      'parser_errors':[r['id'] for r in receipts if 'error' in r],
      'assignments_enumerated':sum('parsed' in r for r in receipts)*5040,
      'distinct_full_questions':len({t['input'] for t in tasks}),
      'distinct_constraint_paragraphs':len({t['input'].split('\nOptions:')[0] for t in tasks}),
      'valid_order_count_range':[min(len(r['valid_orders']) for r in receipts),max(len(r['valid_orders']) for r in receipts)],
      'candidate_counterexamples':sum(r.get('raw_counterexample') is not None for r in receipts),
      'receipts_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'limitations':['historical published outputs, not current-model measurements',
                     'template-specific assistant-authored parser; not arbitrary natural language',
                     'gold labels visible during initial source inspection, but absent from decision inputs',
                     'exhaustive solver supplies the corrected answer; no model retraining or general reasoning improvement',
                     'source claims about original model execution are not independently attested here',
                     'shared runtime and parser remain trusted; no physical or chemical inference']}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'results')
    run(p.parse_args().out)
