import json
from datetime import datetime


FILE_NAME = "expenses.txt"


# ---------------- DATA MANAGEMENT ----------------

def save_data(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# ---------------- INPUT HELPERS ----------------

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount.")


def get_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")


def get_index(expenses, message):
    while True:
        try:
            index = int(input(message))

            if 1 <= index <= len(expenses):
                return index - 1

            print("Invalid index.")

        except ValueError:
            print("Please enter a valid number.")


# ---------------- DISPLAY ----------------

def display_expense(index, expense):
    print(
        f"{index}. {expense['title']} | "
        f"₹{expense['amount']:.2f} | "
        f"{expense['category']} | "
        f"{expense['date']}"
    )


def list_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for index, expense in enumerate(expenses, start=1):
        display_expense(index, expense)


# ---------------- ADD ----------------

def add_expense(expenses):
    title = input("Enter title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    amount = get_amount()

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    date = get_date()

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_data(expenses)

    print("Expense added successfully.")


# ---------------- SEARCH ----------------

def search_expenses(expenses, show_message=True):
    if not expenses:
        print("No expenses found.")
        return []

    search = input("Enter expense to search: ").strip().lower()

    if not search:
        print("Search cannot be empty.")
        return []

    matching_indexes = []

    print("\n========== SEARCH RESULTS ==========")

    for index, expense in enumerate(expenses):
        if search in expense["title"].lower():
            matching_indexes.append(index)
            display_expense(len(matching_indexes), expense)

    if not matching_indexes:
        if show_message:
            print("No matching expenses found.")
        return []

    return matching_indexes


# ---------------- UPDATE ----------------

def update_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    matching_indexes = search_expenses(expenses)

    if not matching_indexes:
        return

    try:
        choice = int(input("Enter result number to update: "))

        if not 1 <= choice <= len(matching_indexes):
            print("Invalid selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    actual_index = matching_indexes[choice - 1]

    old_expense = expenses[actual_index]

    print("\nEnter new details:")

    new_title = input(
        f"Title [{old_expense['title']}]: "
    ).strip()

    if not new_title:
        new_title = old_expense["title"]

    new_amount_input = input(
        f"Amount [{old_expense['amount']}]: "
    ).strip()

    if new_amount_input:
        try:
            new_amount = float(new_amount_input)

            if new_amount <= 0:
                print("Amount must be greater than 0.")
                return

        except ValueError:
            print("Invalid amount.")
            return
    else:
        new_amount = old_expense["amount"]

    new_category = input(
        f"Category [{old_expense['category']}]: "
    ).strip()

    if not new_category:
        new_category = old_expense["category"]

    new_date = input(
        f"Date [{old_expense['date']}] (DD-MM-YYYY): "
    ).strip()

    if new_date:
        try:
            datetime.strptime(new_date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date.")
            return
    else:
        new_date = old_expense["date"]

    expenses[actual_index] = {
        "title": new_title,
        "amount": new_amount,
        "category": new_category,
        "date": new_date
    }

    save_data(expenses)

    print("Expense updated successfully.")


# ---------------- DELETE ----------------

def delete_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    matching_indexes = search_expenses(expenses)

    if not matching_indexes:
        return

    try:
        choice = int(input("Enter result number to delete: "))

        if not 1 <= choice <= len(matching_indexes):
            print("Invalid selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    actual_index = matching_indexes[choice - 1]

    deleted_expense = expenses.pop(actual_index)

    save_data(expenses)

    print(
        f"'{deleted_expense['title']}' "
        f"deleted successfully."
    )


# ---------------- STATISTICS ----------------

def show_stats(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:
        amount = expense["amount"]

        total += amount

        if amount > highest["amount"]:
            highest = expense

        if amount < lowest["amount"]:
            lowest = expense

    average = total / len(expenses)

    print("\n========== EXPENSE STATISTICS ==========")
    print(f"Total Expenses     : ₹{total:.2f}")
    print(f"Number of Expenses : {len(expenses)}")
    print(f"Average Expense    : ₹{average:.2f}")
    print(
        f"Highest Expense    : "
        f"₹{highest['amount']:.2f} ({highest['title']})"
    )
    print(
        f"Lowest Expense     : "
        f"₹{lowest['amount']:.2f} ({lowest['title']})"
    )


# ---------------- CATEGORY SUMMARY ----------------

def category_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")


# ---------------- MONTHLY SUMMARY ----------------

def monthly_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    month = input("Enter month (MM): ").strip()
    year = input("Enter year (YYYY): ").strip()

    if not month.isdigit() or not year.isdigit():
        print("Invalid month or year.")
        return

    if not 1 <= int(month) <= 12:
        print("Invalid month.")
        return

    total = 0
    count = 0

    for expense in expenses:
        date = expense["date"]

        expense_month = date[3:5]
        expense_year = date[6:10]

        if expense_month == month.zfill(2) and expense_year == year:
            total += expense["amount"]
            count += 1

    print("\n========== MONTHLY SUMMARY ==========")
    print(f"Month: {month.zfill(2)}-{year}")
    print(f"Number of Expenses: {count}")
    print(f"Total Spending: ₹{total:.2f}")


# ---------------- MAIN MENU ----------------

def main():
    expenses = load_data()

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Show Statistics")
        print("7. Category Summary")
        print("8. Monthly Summary")
        print("9. Exit")
        print("=====================================")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        match choice:

            case 1:
                add_expense(expenses)

            case 2:
                list_expenses(expenses)

            case 3:
                update_expense(expenses)

            case 4:
                delete_expense(expenses)

            case 5:
                search_expenses(expenses)

            case 6:
                show_stats(expenses)

            case 7:
                category_summary(expenses)

            case 8:
                monthly_summary(expenses)

            case 9:
                print("Thank you for using Expense Tracker.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()