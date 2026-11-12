from app.models import ExpenseCreate

expense = ExpenseCreate(
    title="Lunch",
    amount=55250,
    date="2026-11-12",
    notes="clg lunch",
    category="food"
)

print(expense)
print(expense.model_dump())