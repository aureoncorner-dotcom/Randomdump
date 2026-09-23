"""Repeat review cases against a separately extracted GQG Rune compiler."""
import argparse
import json
import pathlib
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('source_directory', type=pathlib.Path, help='Directory containing compiler.py, finite.py, and geometry.py')
args = parser.parse_args()
source = args.source_directory.resolve()
if not (source / 'compiler.py').is_file():
    parser.error('source_directory must contain compiler.py')
sys.dont_write_bytecode = True
sys.path.insert(0, str(source))
import compiler

for path in sorted((pathlib.Path(__file__).resolve().parent / 'cases').glob('*.gqg')):
    try:
        program, report = compiler.compile_source(path.read_text(encoding='utf-8'))
        result = {
            'case':path.name,
            'verdict':report.splitlines()[0],
            'errors':[{'code':d.code,'message':d.message} for d in program.diagnostics if d.level == 'error'],
            'statuses':{n.name:n.status for n in program.nodes if n.kind in {'DSC','ASN','REF','LOC','QUO'}},
        }
        if path.stem == 'multiple_loci_overwrite':
            import xml.etree.ElementTree as ET
            root = ET.fromstring(program.geometry_svg)
            result['svg_split_labels'] = [n.text for n in root.iter('{http://www.w3.org/2000/svg}text') if (n.text or '').startswith('SPLIT')]
    except Exception as error:
        result = {'case':path.name,'exception':type(error).__name__,'message':str(error)}
    print(json.dumps(result, ensure_ascii=True))
