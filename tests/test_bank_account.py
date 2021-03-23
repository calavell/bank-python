import unittest

class BankAccount:
    opening_balance = 0

    def __init__(self):
        self.balance = BankAccount.opening_balance

    def credit(self, amount):
        self.balance += amount

class test_bank_account(unittest.TestCase):

    def test_credit_1(self):
        account = BankAccount()
        account.credit(10)
        self.assertEqual(account.balance, 10)

if __name__ == '__main__':
    unittest.main()
