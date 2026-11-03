# BUDGET TRACKER

expenses=[]

def add_expenses():
    print("\n--------Add your Expenses---------")
    while True:
        amount=int(input("Enter your expeneses:"))
# asks for expenses untill user enters 0
# stop condition
        if amount == 0:
            print("Finished adding expense!\n")
            break

        expenses.append(amount)
        print(f"{amount} added to your expenses")


def show_summary():
    print("---------Expense Summary---------")
# if no expenses are added
    if not expenses:
        print("No expenses recorded!")

    else:
        print("All expenses recorded:",expenses)
        print(f"Total spent: {sum(expenses)}")


add_expenses()
show_summary()


       