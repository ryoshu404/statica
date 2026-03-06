import argparse
import sys
from pathlib import Path
from statica.pipeline import StaticAnalysisPipeline
from statica.formatters.json_formatter import format_json



def parse_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        prog='statica',
        description='Statica is a format-agnostic analysis pipeline written in Python',
        epilog='github.com/ryoshu404/statica'
    )
    parser.add_argument('path')
    parser.add_argument('-f', '--format', choices=['json'], default='json', help="Format for output, defaults to json.")
    parser.add_argument('-m', '--minlen', type=int, default=6, help='Min length for string recognition, defaults to 6')
    
    return parser.parse_args()

def main():
    
    args = parse_args()
    filepath = Path(args.path).expanduser()
    if not filepath.is_file():
        print(f"Error: {filepath} not found", file=sys.stderr)
        sys.exit(1)
    filepath = filepath.resolve()
    pipeline = StaticAnalysisPipeline(min_string_len=args.minlen)
    report = pipeline.run(filepath)
    match args.format:
        case "json":
            formatted = format_json(report)
    print(formatted)
    
if __name__ == "__main__":
    main()