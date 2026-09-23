"""Verify packaged bytes, execute reference tests and reproduce six fixtures.

No network, physical simulation, or historical empirical reanalysis is performed.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
ABS_TOL=1e-9
REL_TOL=1e-10


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_hashes():
    lines=(ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
    seen=set()
    size=0
    for line in lines:
        checksum,relative=line.split('  ',1)
        if len(checksum)!=64 or any(c not in '0123456789abcdef' for c in checksum):
            raise ValueError('malformed checksum')
        path=(ROOT/relative).resolve()
        if path==ROOT or ROOT not in path.parents or relative in seen:
            raise ValueError('duplicate or unsafe packaged path')
        seen.add(relative)
        if not path.is_file() or digest(path)!=checksum:
            raise ValueError(f'missing or changed packaged file: {relative}')
        size+=path.stat().st_size
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    extras=sorted(actual-seen-{'SHA256SUMS.txt'})
    executable_suffixes={'.py','.pyw','.pyc','.pyd','.so','.dll'}
    if any(name.startswith('reference/') and Path(name).suffix.lower() in executable_suffixes for name in extras):
        raise ValueError('unexpected executable or bytecode on the reference import path')
    return {'status':'PASS','files_checked':len(seen),'bytes_checked':size,'unlisted_files':extras}


def close_value(actual,expected,address='root'):
    if isinstance(expected,dict):
        if not isinstance(actual,dict) or set(actual)!=set(expected):raise ValueError(f'JSON key mismatch at {address}')
        for key in expected:close_value(actual[key],expected[key],address+'.'+key)
    elif isinstance(expected,list):
        if not isinstance(actual,list) or len(actual)!=len(expected):raise ValueError(f'JSON length mismatch at {address}')
        for i,(a,b) in enumerate(zip(actual,expected)):close_value(a,b,f'{address}[{i}]')
    elif type(expected) is float:
        if type(actual) not in (float,int) or not math.isfinite(actual) or not math.isclose(actual,expected,rel_tol=REL_TOL,abs_tol=ABS_TOL):
            raise ValueError(f'numeric mismatch at {address}: {actual} versus {expected}')
    elif type(actual) is not type(expected) or actual!=expected:
        raise ValueError(f'value mismatch at {address}')


def compare_throat(actual,expected):
    if actual.suffix=='.json':
        close_value(json.loads(actual.read_text(encoding='utf-8')),json.loads(expected.read_text(encoding='utf-8')))
    elif actual.suffix=='.csv':
        a=list(csv.reader(io.StringIO(actual.read_text(encoding='utf-8'))))
        b=list(csv.reader(io.StringIO(expected.read_text(encoding='utf-8'))))
        if len(a)!=len(b) or a[0]!=b[0]:raise ValueError('profile CSV shape mismatch')
        for i,(left,right) in enumerate(zip(a[1:],b[1:])):
            if len(left)!=len(right):raise ValueError('profile CSV row width mismatch')
            for j,(x,y) in enumerate(zip(left,right)):close_value(float(x),float(y),f'csv[{i},{j}]')
    elif actual.read_bytes()!=expected.read_bytes():
        raise ValueError('unexpected numerical artifact mismatch')


def run_reference_checks():
    sys.dont_write_bytecode = True
    sys.path.insert(0,str(ROOT/'reference'))
    suite=unittest.defaultTestLoader.discover(str(ROOT/'reference'),pattern='test_*.py')
    output=io.StringIO()
    result=unittest.TextTestRunner(stream=output,verbosity=1).run(suite)
    if not result.wasSuccessful():raise ValueError('reference suite failed:\n'+output.getvalue())
    from lattice_validator import run_fixture
    from throat import write_run
    reproductions=[]
    numerical=[]
    with tempfile.TemporaryDirectory(prefix='toroidal-reference-') as directory:
        for name in ('cubic','rectangular','translated_rectangular','throat','throat_flat','throat_translated'):
            config=json.loads((ROOT/'configs'/f'{name}.json').read_text(encoding='utf-8'))
            temporary=Path(directory)/name
            is_throat=name.startswith('throat')
            report=(write_run if is_throat else run_fixture)(config,temporary)
            if report['status']!='PASS':raise ValueError(f'fixture failed: {name}')
            expected=ROOT/'examples'/name
            generated={p.name for p in temporary.iterdir() if p.is_file()}
            stored={p.name for p in expected.iterdir() if p.is_file()}
            if generated!=stored:raise ValueError(f'example files differ: {name}')
            byte_identical=True
            for filename in sorted(generated):
                a,b=temporary/filename,expected/filename
                same=a.read_bytes()==b.read_bytes()
                byte_identical=byte_identical and same
                if is_throat:compare_throat(a,b)
                elif not same:raise ValueError(f'exact artifact differs: {name}/{filename}')
            reproductions.append({'example':name,'status':'PASS','files_compared':len(generated),
                'comparison':'numeric tolerance and exact structure' if is_throat else 'byte exact',
                'byte_identical_on_this_runtime':byte_identical})
            if is_throat:numerical.append({'example':name,'report':report})
    return {'status':'PASS','unit_tests':{'run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped)},
            'example_reproductions':reproductions,'throat_checks':numerical,
            'numeric_reproduction_tolerances':{'absolute':ABS_TOL,'relative':REL_TOL},
            'scope':'new deterministic references only; no historical empirical reanalysis'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true',help='print the complete verification record')
    args=parser.parse_args()
    try:
        hashes=verify_hashes()
        checks=run_reference_checks()
        result={'status':'PASS','integrity':hashes,'reference_checks':checks}
    except (ValueError,OSError,ArithmeticError) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)},indent=2))
        return 1
    if args.json:print(json.dumps(result,indent=2,sort_keys=True))
    else:print(f"PASS: {hashes['files_checked']} file hashes, {checks['unit_tests']['run']} tests, six reproduced examples. Physical experiments: NOT_RUN.")
    return 0


if __name__=='__main__':raise SystemExit(main())
