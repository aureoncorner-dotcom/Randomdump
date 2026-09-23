"""Run the regression and exact finite checks; write a compact verification receipt."""
import json
from pathlib import Path
import sys
import unittest

if __name__=='__main__':
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root/'tests'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    counts = sys.modules['test_gqg'].COUNTS
    receipt = {'python':sys.version.split()[0],'tests':result.testsRun,'success':result.wasSuccessful(),
               'failures':len(result.failures),'errors':len(result.errors),'exact_case_counts':counts,
               'scope':'finite model regression checks; no external empirical replay or unbounded-domain theorem verification'}
    (root/'VERIFICATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    sys.exit(0 if result.wasSuccessful() else 1)
