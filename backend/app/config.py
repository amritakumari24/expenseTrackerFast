from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR/"data"
CSV_FILE = DATA_DIR/"expenses.csv"
DATA_DIR.mkdir(parents=True, exist_ok=True)


CSV_HEADERS= [
"id",
"title",
"amount",
"category",
"date",
"notes"

]