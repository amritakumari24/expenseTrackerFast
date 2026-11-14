from app.models import ExpenseCreate
from app.services import add_expense

expense = ExpenseCreate(

    title=" Lunch",
    amount=123,
    category="Food",
    date="2026-11-14",
    notes="hostel lunch"
)

result = add_expense(expense)
print(result)