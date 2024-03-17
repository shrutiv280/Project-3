import json
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, amount, description, category):
        self.expenses.append({
            'amount': amount,
            'description': description,
            'category': category
        })
        self.categories.add(category)

    def monthly_summary(self):
        monthly_expenses = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category in monthly_expenses:
                monthly_expenses[category] += amount
            else:
                monthly_expenses[category] = amount
        return monthly_expenses

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)

    def load_expenses(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
                for expense in self.expenses:
                    self.categories.add(expense['category'])

# Function to display menu
def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. Save Expenses")
    print("4. Load Expenses")
    print("5. Exit")

# Function to get user input for adding expense
def get_expense_input():
    amount = float(input("Enter amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category: ")
    return amount, description, category

# Main function to interact with the Expense Tracker
def main():
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount, description, category = get_expense_input()
            tracker.add_expense(amount, description, category)
            print("Expense added successfully!")
        elif choice == '2':
            print("\nMonthly Summary:")
            summary = tracker.monthly_summary()
            for category, amount in summary.items():
                print(f"{category}: ${amount}")
        elif choice == '3':
            filename = input("Enter filename to save expenses: ")
            tracker.save_expenses(filename)
            print("Expenses saved successfully!")
        elif choice == '4':
            filename = input("Enter filename to load expenses: ")
            tracker.load_expenses(filename)
            print("Expenses loaded successfully!")
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
