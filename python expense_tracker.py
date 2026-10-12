
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if expense_date == "":
        expense_date = str(date.today())

    try:
        date.fromisoformat(expense_date)
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category (Food/Travel/Shopping/etc.): ")
        description = input("Enter description: ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [expense_date, category, description, amount]
            )

        print("Expense added successfully!")

    except ValueError:
        print("Invalid date or amount. Please try again.")


def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            expense["Date"], "|",
            expense["Category"], "|",
            expense["Description"], "| Rs.",
            expense["Amount"]
        )


def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n--- Filtered Expenses ---")
        for expense in reader:
            if expense["Category"].lower() == category:
                print(expense)
                found = True

    if not found:
        print("No expenses found in this category.")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])
            summary[category] = summary.get(category, 0) + amount

    print("\n--- Category Summary ---")
    if not summary:
        print("No expenses recorded.")
        return

    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")

    grand_total = sum(summary.values())
    print(f"Total Expenses: Rs. {grand_total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
