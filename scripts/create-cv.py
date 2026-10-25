"""Build the internship CV with linked certificate documents."""
from pathlib import Path
from cv_layout import build_cv

if __name__ == '__main__':
    build_cv(Path(__file__).resolve().parents[1])
