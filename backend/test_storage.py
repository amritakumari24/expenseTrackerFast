from app.utils import initialize_csv , read_expenses

initialize_csv()

df = read_expenses()
print(df)

print("\nCSV storage working successfully!")
