import numpy as np
from validity import *

class User:
    project = "Expense Tracker"
    
    def __init__(self, username):
        self.username = username
        self.balance = 0.0
        self.budget = 0.0
        self.income = []
        self.expense = []
        self.categories = ("Food", "Transport", "Bills", "Health", "Shopping", "Education", "Other")
        
    def add_income(self, amount, date):
        self.income.append({"amount": amount, "date": date})
        self.balance += amount

    def add_expense(self, amount, category, date):
        self.expense.append({
            "amount"  : amount,
            "category": category,
            "date"    : date
        })
        self.balance -= amount
    
    def total_income(self):
        total = 0.0
        for e in self.income:
            total = total + e["amount"]
        return total

    def total_expense(self):
        total = 0.0
        for e in self.expense:
            total = total + e["amount"]
        return total

    def add_entry(self):
        print("\n Adding Entry:")
        print("1.Income")
        print("2.Expense")
        choice = get_valid_int("  Choose: ", 1, 2)
        amount = get_valid_float("  Amount (BDT): ")
        date = get_valid_date("  Date (DD-MM-YYYY): ")

        if choice == 1:
            self.add_income(amount, date)
            print("Income added!")
        else:
            print("\n Available Categories:")
            for i, cat in enumerate(self.categories, 1):
               print(f"{i}. {cat}")
        
            choice_cat = get_valid_int("\nChoose category number: ", 1, len(self.categories))
            category   = self.categories[choice_cat - 1]
                
            self.add_expense(amount, category, date)
            print("Expense added!")

    def delete_entry(self):
        print("\n Delete Entry: ")
        print("1.Income entry")
        print("2.Expense entry")
        choice = get_valid_int("  Choose: ", 1, 2)
        entry_type = "income" if choice == 1 else "expense"
        entries = self.income if choice == 1 else self.expense

        if not entries:
            print(" No entries to delete.")
            return

        for i, e in enumerate(entries, 1):
            if entry_type == "income":
                print(f"{i}. {e['date']}  +{e['amount']:.2f} BDT")
            else:
                print(f"{i}. {e['date']}  [{e['category']}]  -{e['amount']:.2f} BDT")

        idx = get_valid_int("Enter number to delete: ", 1, len(entries))
        entries.pop(idx - 1)
        print("Entry deleted!")
        
    def show_statistics(user):
        print("\n Statistics: ")
        if not user.expense:
            print("No expense data available.")
            return
        amounts = np.array([e["amount"] for e in user.expense])
        
        print(f"Total Expense: {np.sum(amounts):.2f} BDT")
        print(f"Average Expense: {np.mean(amounts):.2f} BDT")
        print(f"Highest Entry: {np.max(amounts):.2f} BDT")
        print(f"Lowest Entry: {np.min(amounts):.2f} BDT")
        print(f"Categories Used: {user.categories}")