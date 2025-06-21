from pathlib import Path

# base
BASE_DIR = Path(__file__).resolve().parent

# input paths
DATA_DIR = BASE_DIR / "data" / "raw_chunks"
METADATA_PATH = BASE_DIR / "data" / "kafka_metadata.csv"

# output paths
OUTPUT_DIR = BASE_DIR / "results"
VISUALS_DIR = OUTPUT_DIR / "visualizations"
CSV_DIR = OUTPUT_DIR / "csv_outputs"

# modeling parameters
NUM_TOPICS = 10
MAX_DF = 0.95
MIN_DF = 5

for path in [OUTPUT_DIR, VISUALS_DIR, CSV_DIR]:
    path.mkdir(parents=True, exist_ok=True)

print("Loaded config. Output folders exist already or are created.")