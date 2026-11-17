from fastapi import FastAPI ,HTTPException

from app.models import ExpenseCreate , Expense 
from app.services import (
    add_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense
)

from app.utils import initialize_csv


app = FastAPI(
    title="Expense Tracker API",
    description="A simple API to manage personal expenses",
    version="1.0.0"

)

initialize_csv()

@app.post("/expenses", response_model=Expense)
def create_expense(expense:ExpenseCreate):
    return add_expense(expense)


@app.get("/expenses")
def read_expenses():
    return get_all_expenses()


@app.get("/expenses/{expense_id}", response_model=Expense)
def read_expense(expense_id: int):
    expense = get_expense_by_id(expense_id)
    if expense is None:
        raise HTTPException(
            status_code=404,
            detail ="Expense not found"

        )
    return expense

@app.put("/expenses/{expense_id}", response_model=Expense)
def edit_expense(expense_id:int, updated_expense:ExpenseCreate):
    expense = update_expense(expense_id, updated_expense)
    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"

        )
    return expense

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id:int):
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
        status_code=404,
        detail="expense not found"
        )
    return{
        "message": "Expense deleted successfully!"
    }

from app.analytics import get_total_spending
@app.get("/analytics/total")
def total_spending():
    total = get_total_spending()
    return {"total_spending" : total}

from app.analytics import get_category_spending
@app.get("/analytics/category")
def category_spending():
    result = get_category_spending()
    return {
        "category_spending": result 
    }


from app.analytics import get_average_expense
@app.get("/analytics/average")
def average_expense():
    average = get_average_expense()
    return {
        "average expense" : average
    }


from app.analytics import get_monthly_spending
@app.get("/analytics/monthly")
def monthly_spending():
    result = get_monthly_spending()
    return {

        "monthly spending": result
    }