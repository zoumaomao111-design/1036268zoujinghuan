# Student Name: ZOU JINGHUAN
# Student Number: 1036268
# Project Title: Milestone Project #1 – Weekly Budget & Expense Tracker
# Date: March 2026

def print_title():
    print("=" * 55)
    print("      WEEKLY BUDGET & EXPENSE TRACKER")
    print("=" * 55)


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a value of 0 or more.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_category():
    while True:
        print("\nSelect a category:")
        print("1. Food")
        print("2. Transport")
        print("3. Study")
        print("4. Entertainment")
        print("5. Other")

        choice = input("Enter option (1-5): ")

        if choice == "1":
            return "Food"
        elif choice == "2":
            return "Transport"
        elif choice == "3":
            return "Study"
        elif choice == "4":
            return "Entertainment"
        elif choice == "5":
            return "Other"
        else:
            print("Invalid option. Please choose between 1 and 5.")


def add_expense(expenses, categories):
    amount = get_positive_float("Enter expense amount: $")
    category = get_category()

    expenses.append(amount)
    categories.append(category)

    print(f"Expense of ${amount:.2f} added under {category}.")


def show_summary(expenses, budget):
    if len(expenses) == 0:
        print("\nNo expenses have been entered yet.")
        return

    total = sum(expenses)
    average = total / len(expenses)
    highest = max(expenses)
    remaining = budget - total

    print("\n" + "=" * 40)
    print("EXPENSE SUMMARY")
    print("=" * 40)
    print(f"Weekly budget:      ${budget:.2f}")
    print(f"Total spent:        ${total:.2f}")
    print(f"Average expense:    ${average:.2f}")
    print(f"Highest expense:    ${highest:.2f}")
    print(f"Remaining budget:   ${remaining:.2f}")

    if total > budget:
        print("Status: You are OVER budget.")
    elif total == budget:
        print("Status: You have used your full budget.")
    else:
        print("Status: You are within budget.")


def show_all_expenses(expenses, categories):
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 40)
    print("ALL EXPENSES")
    print("=" * 40)

    for i in range(len(expenses)):
        print(f"{i + 1}. ${expenses[i]:.2f} - {categories[i]}")


def show_category_totals(expenses, categories):
    if len(expenses) == 0:
        print("\nNo expenses recorded yet.")
        return

    food_total = 0
    transport_total = 0
    study_total = 0
    entertainment_total = 0
    other_total = 0

    for i in range(len(expenses)):
        if categories[i] == "Food":
            food_total += expenses[i]
        elif categories[i] == "Transport":
            transport_total += expenses[i]
        elif categories[i] == "Study":
            study_total += expenses[i]
        elif categories[i] == "Entertainment":
            entertainment_total += expenses[i]
        else:
            other_total += expenses[i]

    print("\n" + "=" * 40)
    print("CATEGORY TOTALS")
    print("=" * 40)
    print(f"Food:           ${food_total:.2f}")
    print(f"Transport:      ${transport_total:.2f}")
    print(f"Study:          ${study_total:.2f}")
    print(f"Entertainment:  ${entertainment_total:.2f}")
    print(f"Other:          ${other_total:.2f}")


def show_menu():
    print("\nChoose an option:")
    print("1. Add expense")
    print("2. Show summary")
    print("3. Show all expenses")
    print("4. Show category totals")
    print("5. Exit")


def main():
    print_title()

    budget = get_positive_float("Enter your weekly budget: $")

    expenses = []
    categories = []

    option = ""

    while option != "5":
        show_menu()
        option = input("Enter option (1-5): ")

        if option == "1":
            add_expense(expenses, categories)
        elif option == "2":
            show_summary(expenses, budget)
        elif option == "3":
            show_all_expenses(expenses, categories)
        elif option == "4":
            show_category_totals(expenses, categories)
        elif option == "5":
            print("\nThank you for using the Weekly Budget & Expense Tracker.")
            print("Goodbye.")
        else:
            print("Invalid menu option. Please choose between 1 and 5.")


main()
