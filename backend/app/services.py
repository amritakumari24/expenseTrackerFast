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
    