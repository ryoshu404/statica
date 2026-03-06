import argparse
import sys
from pathlib import Path
from statica.pipeline import StaticAnalysisPipeline
from statica.formatters.json_formatter import format_json
import importlib.metadata

try:
    VERSION = importlib.metadata.version('statica')
except importlib.metadata.PackageNotFoundError:
    VERSION = 'unknown'

def parse_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        prog='statica',
        description='Statica - modular static analysis pipeline',
        epilog='https://github.com/ryoshu404/statica',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('path', help="Path to file to analyze")
    parser.add_argument('-f', '--format', choices=['json'], default='json', help='Output format')
    parser.add_argument('-m', '--minlen', type=int, default=6, help='Min length for string recognition')
    parser.add_argument("-v", '--version', action='version', version=f'statica {VERSION}')
    
    return parser.parse_args()

def main():
    
    args = parse_args()
    filepath = Path(args.path).expanduser()
    if not filepath.is_file():
        print(f'Error: {filepath} not found', file=sys.stderr)
        sys.exit(1)
    filepath = filepath.resolve()
    pipeline = StaticAnalysisPipeline(min_string_len=args.minlen)
    report = pipeline.run(filepath, VERSION)
    match args.format:
        case 'json':
            formatted = format_json(report)
    print(formatted)
    
if __name__ == '__main__':
    main()