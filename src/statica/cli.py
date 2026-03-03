import argparse
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        prog='Statica',
        description='Statica is a format-agnostic analysis pipeline written in Python',
        epilog='github.com/ryoshu404/statica'
    )
    parser.add_argument('path')
    parser.add_argument('-f', '--format', choices=['json'], default='json', help="Format for output, defaults to json.")
    return parser.parse_args()

def main():
    args = parse_args()
    filepath = Path(args.path)
    if filepath.exists() and filepath.is_file():
        print("valid file")
    else:
        print(f"Error: {filepath} not found", file=sys.stderr)
        sys.exit(1)
    

if __name__ == "__main__":
    main()