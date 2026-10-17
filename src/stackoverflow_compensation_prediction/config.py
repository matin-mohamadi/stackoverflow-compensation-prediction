from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

# data folder
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
SO_DATA_RAW = RAW_DATA_DIR / "stack_overflow_2025"

# dataset path
DATA_PATH = SO_DATA_RAW / "survey_results_public.csv"
SCHEMA_DATA_PATH = SO_DATA_RAW / "survey_results_schema.csv"
