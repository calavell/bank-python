class BankAccount:
    opening_balance = 0

    def __init__(self):
        self.balance = opening_balance

    def withdraw(self, amount):
        self.balance += amount
