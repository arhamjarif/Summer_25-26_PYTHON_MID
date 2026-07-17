from validity import get_valid_float
def set_budget(user):
    print("\n --- Set Budget ---")
    user.budget = get_valid_float("Enter Budget Limit (BDT): ")
    print(f"  Budget set to {user.budget:.2f} BDT.")



def search_by_category(user):
    print("\n --- Search by Category ---")

    if not user.expense:
        print("  No expense entries found.")
        return

    used = sorted(set(e["category"] for e in user.expense))
    print(f"  Categories used: {', '.join(used)}")
    keyword = input("  Enter category to search: ").strip().capitalize()

    if keyword not in user.categories:
        print(f"  No expenses found for category '{keyword}'.")
        return  
    
    print (f"\n  Expenses in category '{keyword}':")
    total = 0
    for expense in user.expense:
        if expense["category"] == keyword:
            print(f"    - {expense['date']}: {expense['amount']:.2f} BDT")
            total += expense["amount"]
    print(f"  Total for category '{keyword}': {total:.2f} BDT")

def view_history(user):
        print("\n History:")
        print("\nIncome:")
        if user.income:
            for i, e in enumerate(user.income, 1):
                print(f"{i}. {e['date']}  +{e['amount']:.2f} BDT")
        else:
            print("No income entries.")

        print("\nExpense:")
        if user.expense:
            for i, e in enumerate(user.expense, 1):
                print(f"{i}. {e['date']}  [{e['category']}]  -{e['amount']:.2f} BDT")
        else:
            print("No expense entries.")