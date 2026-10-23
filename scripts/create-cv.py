"""Build the verified one-page internship CV."""
from pathlib import Path
from cv_layout import build_cv

if __name__ == '__main__':
    build_cv(Path(__file__).resolve().parents[1])
