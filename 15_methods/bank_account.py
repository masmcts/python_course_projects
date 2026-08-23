class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

account = BankAccount("Ali", 1000)
account.deposit(500)
account.withdraw(200)
print(account.owner, account.balance)
BankAccount.change_bank_name("New Python Bank")
print(BankAccount.bank_name)
