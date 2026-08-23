"""
account.py - Account class and custom exception.
Part of Project 3: Bank Account Manager (SOLUTION)
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal or transfer exceeds the available balance."""
    pass


class Account:
    # Class attributes: shared across every Account instance
    bank_name = "PyBank"
    interest_rate = 0.02

    def __init__(self, owner, balance=0):
        # Instance attributes: unique to each account
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"{self.owner} has ${self.balance:.2f}, cannot withdraw ${amount:.2f}."
            )
        self.balance -= amount

    def apply_interest(self):
        """Stretch goal: apply the class-level interest rate to this account."""
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"{self.owner} — ${self.balance:.2f}"


def transfer(sender, receiver, amount):
    """Move money from sender to receiver. If withdrawal fails, deposit never happens."""
    sender.withdraw(amount)   # raises if this fails; receiver.deposit is never reached
    receiver.deposit(amount)
