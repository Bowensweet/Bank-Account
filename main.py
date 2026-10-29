from bank_account import BankAccount


def display_menu():
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")


def get_amount(prompt):
    # Prompt for a dollar amount. Returns a float, or None if invalid.
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None


def make_deposit(account):
    print()
    amount = get_amount("How much would you like to deposit? ")
    if amount is None:
        return
    if account.deposit(amount):
        print(f"Deposited ${amount:,.2f}.")
    else:
        print("Deposit must be greater than $0.00.")


def make_withdrawal(account):
    print()
    amount = get_amount("How much would you like to withdraw? ")
    if amount is None:
        return
    if account.withdraw(amount):
        print(f"Withdrew ${amount:,.2f}.")
    elif amount <= 0:
        print("Withdrawal must be greater than $0.00.")
    else:
        print(f"Insufficient funds. Your balance is ${account.get_balance():,.2f}.")


def view_account_information(account):
    print()
    print(f"Name: {account.customer_name}")
    print(f"Account #: {account.account_number}")
    print(f"Balance: ${account.get_balance():,.2f}")


def main():
    print("Welcome to Bowen Bank, you broke boi!")
    name = input("Please enter your name: ")
    account = BankAccount(name)

    while True:
        display_menu()
        choice = input("Please choose an option:")

        if choice == "1":
            make_deposit(account)
        elif choice == "2":
            make_withdrawal(account)
        elif choice == "3":
            view_account_information(account)
        elif choice == "4":
            print()
            print("Thank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()