from manager import ExpenseManager

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")

def main():
    manager = ExpenseManager()
    filename = "expenses.txt"

    manager.load_from_file(filename)

    while True:
        print("\n--- Financial Analyzer ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Statistics")
        print("4. Save & Exit")

        choice = input("Enter option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = get_valid_float("Enter amount: $")
            manager.add_expense(date, category, amount)
            print("Expense added.")

        elif choice == "2":
            manager.show_expenses()

        elif choice == "3":
            manager.show_statistics()

        elif choice == "4":
            manager.save_to_file(filename)
            print("Data saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
