import pandas as pd 
import numpy as np 

from app.utils import read_expenses


def get_total_spending():
    df = read_expenses()

    if df.empty:
        return 0
    total = df["amount"].sum()
    return float(total)