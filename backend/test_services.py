# from app.models import ExpenseCreate
# from app.services import add_expense

# expense = ExpenseCreate(

#     title=" Lunch",
#     amount=123,
#     category="Food",
#     date="2026-11-14",
#     notes="hostel lunch"
# )

# result = add_expense(expense)
# print(result)

# from app.services import get_all_expenses, get_expense_by_id

# print("ALL EXPENSES: ")
# print(get_all_expenses())

# print("\n EXPENSE WITH ID 1:")
# print(get_expense_by_id(1))

# print("\nEXPENSE WITH ID 99:")
# print(get_expense_by_id(99))


# from app.models import ExpenseCreate
# from app.services import update_expense, get_all_expenses

# updated_data = ExpenseCreate(
#  title="lunch",
#  amount=156,
#  category="food",
#  date="2026-11-14",
#  notes="updated hostel lunch"



# )

# result = update_expense(1, updated_data)

# print("UPDATED EXPENSE: ")
# print(result )



from app.services import delete_expense, get_all_expenses

print("BEFORE DELETE:")
print(get_all_expenses())

print("\nDELETE EXPENSE WITH ID 1:")
print(delete_expense(1))

print("\nAFTER DELETE ")
print(get_all_expenses())

print("\n DELETE NON-EXITING ID 99")
print(delete_expense(99))
