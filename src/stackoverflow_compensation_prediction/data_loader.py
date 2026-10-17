import requests
from tqdm import tqdm

from stackoverflow_compensation_prediction.config import (
    DATA_PATH,
    SCHEMA_DATA_PATH,
)

# official 2026 dataset links (GitHub LFS media)
SCHEMA_URL = "https://media.githubusercontent.com/media/StackExchange/Survey/main/packages/archive/2026/survey_results_schema.csv"
DATA_URL = "https://media.githubusercontent.com/media/StackExchange/Survey/main/packages/archive/2026/survey_results_public.csv"


def download_file(url: str, target_path):
    # create data/raw/stack_overflow_2025 folder if it does not exist
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # use a temp file name so broken downloads don`t stay
    temp_path = target_path.with_suffix(".part")

    print(f"Downloading {target_path.name}...")
    response = requests.get(url, stream=True, timeout=300)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))

    with (
        open(temp_path, "wb") as file,
        tqdm(total=total_size, unit="B", unit_scale=True) as bar,
    ):
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

    # rename temp file to final csv file when finished
    temp_path.rename(target_path)
    print(f"Saved to {target_path}")


def ensure_data_exists():
    # check schema file
    if not SCHEMA_DATA_PATH.exists():
        download_file(SCHEMA_URL, SCHEMA_DATA_PATH)
    else:
        print("Schema file already exists.")

    # check main dataset file
    if not DATA_PATH.exists():
        download_file(DATA_URL, DATA_PATH)
    else:
        print("Dataset file already exists.")


if __name__ == "__main__":
    ensure_data_exists()
