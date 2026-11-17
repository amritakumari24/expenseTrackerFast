import pandas as pd 
import numpy as np 

from app.utils import read_expenses


def get_total_spending():
    df = read_expenses()

    if df.empty:
        return 0
    total = df["amount"].sum()
    return float(total)

def get_category_spending():
    df = read_expenses()
    if df.empty:
        return {}
    category_totals = df.groupby("category")["amount"].sum()
    return category_totals.to_dict()


def get_average_expense():
    df = read_expenses()

    if df.empty:
        return 0
    average = np.mean(df["amount"])
    return float(average)


def get_monthly_spending():
    df = read_expenses()

    if df.empty:
        return {}

    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.to_period("M")

    monthly_totals = df.groupby("month")["amount"].sum()

    return {

      str(month): float(amount)
      for month, amount in monthly_totals.items()

    }