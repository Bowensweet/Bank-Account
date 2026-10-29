import random


class BankAccount:
    # Represents a customer's bank account.

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
       # Add money to the account. Returns True if successful.
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        # Remove money from the account. Returns True if successful.
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        # Get the current balance of the account.
        return self.balance