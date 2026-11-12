import pandas as pd
from app.config import CSV_FILE, CSV_HEADERS

def read_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=CSV_HEADERS)


def save_expenses(df):
    df.to_csv(CSV_FILE, index=False)



def initialize_csv():
    """
    Create CSV file if it does not exist
    or if it is empty.
    """

    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        df = pd.DataFrame(columns=CSV_HEADERS)
        save_expenses(df)

