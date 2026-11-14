import pandas as pd

from app.models import ExpenseCreate, Expense
from app.utils import read_expenses, save_expenses

def add_expense(expense: ExpenseCreate):
    df = read_expenses()

    if df.empty:
        new_id = 1
    else:
        new_id = int(df["id"].max()) +1

    expense_data = expense.model_dump(mode="json")
    expense_data["id"] = new_id

    new_row = pd.DataFrame([expense_data])

    df = pd.concat([df, new_row], ignore_index=True)
    save_expenses(df)

    return Expense(**expense_data)    



def get_all_expenses():
    df = read_expenses()
    return df.to_dict(orient="records")  


def get_expense_by_id(expense_id:int):
    df = read_expenses()

    expense = df[df["id"] == expense_id]

    if expense.empty:
        return None
    return expense.iloc[0].to_dict()



def update_expense(expense_id:int, updated_expense: ExpenseCreate):
    df = read_expenses()

    if expense_id not in df["id"].values:
        return None

    expense_data = updated_expense.model_dump(mode="json")
    expense_data["id"] = expense_id

    df.loc[
        df["id"]== expense_id,
        list(expense_data.keys())
        

    ] = list(expense_data.values())

    save_expenses(df)
    return Expense(**expense_data)
   


def delete_expense(expense_id:int):
    df = read_expenses()

    if expense_id not in df["id"].values:
        return False

    df = df[df["id"] != expense_id]

    save_expenses(df)
    return True

    