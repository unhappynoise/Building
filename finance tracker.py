class Finance:
    def __init__(self, expenses=None, balance=0, income=0):
        if expenses is None:
            self.expenses = []
        else:
            self.expenses = expenses
        self.income = income
        self.balance = balance


    def add_income(self):
        amount = float(input("Enter amount to be added to income: "))

        self.income = self.income + amount

    def add_expense(self):
        description = input("What is the expense? ")

        amount = float(input("Enter amount to be added to income: "))
        self.expenses.append({'description': description, 'amount': amount})

    def view_transactions(self):
        print("\nIncome: ")
        print(f"Total Income: ${self.income}")

        print("\nExpenses:")
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for idx, expense in enumerate(self.expenses, 1):
                print(f"{idx}. {expense['description']} - ${expense['amount']}")

    def cal_balance(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        self.balance = self.income - total_expenses

        print(f"Your balance is ${self.balance}")

def main():
    tracker = Finance()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_income()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.cal_balance()
        elif choice == "4":
            tracker.view_transactions()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()


