"""Build the one-page CV with linked certificate documents."""
from pathlib import Path
import argparse
import json
from cv_layout import build_cv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--private-reference', type=Path,
                        help='Local JSON reference details; writes only to ignored output/pdf.')
    args = parser.parse_args()
    reference = json.loads(args.private_reference.read_text(encoding='utf-8')) if args.private_reference else None
    build_cv(Path(__file__).resolve().parents[1], private_reference=reference)
