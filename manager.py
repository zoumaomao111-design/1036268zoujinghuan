from expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    # Load from TXT file
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    date, category, amount = line.split(",")
                    self.expenses.append(Expense(date, category, float(amount)))
        except FileNotFoundError:
            print("No existing data found. Starting fresh.")

    # Save to TXT file
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for exp in self.expenses:
                f.write(f"{exp.date},{exp.category},{exp.amount}\n")

    # Add new expense
    def add_expense(self, date, category, amount):
        self.expenses.append(Expense(date, category, amount))

    # Display all expenses
    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for exp in self.expenses:
            print(exp)

    # Statistics
    def show_statistics(self):
        if not self.expenses:
            print("No data available.")
            return

        total = sum(exp.amount for exp in self.expenses)
        avg = total / len(self.expenses)
        highest = max(self.expenses, key=lambda x: x.amount)
        lowest = min(self.expenses, key=lambda x: x.amount)

        print("\n--- Expense Statistics ---")
        print(f"Total Spending: ${total:.2f}")
        print(f"Average Spending: ${avg:.2f}")
        print(f"Highest Expense: {highest.category} - ${highest.amount}")
        print(f"Lowest Expense: {lowest.category} - ${lowest.amount}")
