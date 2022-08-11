import sys

def show_balance(balance):
    print("Current Balance: $" + format_balance(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if balance < float(amount):
        print("Insufficient funds!")
        return balance
    else:
        return balance - float(amount)


def logout(name):
    print("Goodbye", name + "!")
    sys.exit()


def format_balance(bal):
    return "{:,.2f}".format(bal)
