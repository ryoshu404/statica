import argparse
import sys
import json
from pathlib import Path
from statica.pipeline import StaticAnalysisPipeline

def parse_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        prog='statica',
        description='Statica is a format-agnostic analysis pipeline written in Python',
        epilog='github.com/ryoshu404/statica'
    )
    parser.add_argument('path')
    parser.add_argument('-f', '--format', choices=['json'], default='json', help="Format for output, defaults to json.")
    
    return parser.parse_args()

def main():
    
    args = parse_args()
    filepath = Path(args.path).expanduser()
    if not filepath.is_file():
        print(f"Error: {filepath} not found", file=sys.stderr)
        sys.exit(1)
    filepath = filepath.resolve()
    pipeline = StaticAnalysisPipeline()
    report = pipeline.run(filepath)
    
if __name__ == "__main__":
    main()