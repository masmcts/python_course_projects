# Project 3: Bank Account Manager (OOP)
**Week 2 Capstone — Topics: Scope, Modules, OOP Basics, Classes, Attributes, Methods, Exceptions, File Handling**

## Goal
Build a bank account system using classes. Accounts can deposit, withdraw,
and transfer money, with proper error handling, and the data is saved to a
file so it persists between runs.

## What You'll Practice
- Classes and objects (`Account`)
- Instance attributes (balance, owner) vs. class attributes (bank name, interest rate)
- Methods (`deposit`, `withdraw`, `transfer`)
- Exceptions (`try`/`except`) for insufficient funds or bad input
- File handling (saving/loading account data as text)
- Splitting code across modules (`utils.py` imported into `main.py`)

## Requirements

### 1. `Account` class (in `account.py`)
```python
class Account:
    bank_name = "PyBank"          # class attribute — shared by all accounts
    interest_rate = 0.02          # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner        # instance attribute
        self.balance = balance    # instance attribute
```

- `deposit(amount)`: raises `ValueError` if amount <= 0; otherwise adds to balance.
- `withdraw(amount)`: raises a custom `InsufficientFundsError` if amount > balance;
  raises `ValueError` if amount <= 0; otherwise subtracts from balance.
- `__str__`: returns a readable string like `"Alice — $150.00"`.

### 2. Custom exception
```python
class InsufficientFundsError(Exception):
    pass
```

### 3. Transfer function
A standalone function `transfer(sender, receiver, amount)` that withdraws
from one account and deposits into another — and if the withdrawal fails,
the deposit should never happen.

### 4. File persistence (`storage.py`)
- `save_accounts(accounts, filename)`: write each account as a line of text
  (e.g. `"Alice,150.00"`).
- `load_accounts(filename)`: read the file back and reconstruct a list of
  `Account` objects. Handle the case where the file doesn't exist yet
  (use `try`/`except FileNotFoundError`, return an empty list).

### 5. `main.py`
Ties it together with a menu: create account, deposit, withdraw, transfer,
view all accounts, save & quit.

## Step-by-Step Guide

1. Start with the `Account` class and test creating a couple of instances
   in a scratch script before building the menu.
2. Add `deposit`/`withdraw`, testing edge cases (negative amounts, overdraft)
   in isolation.
3. Add the custom exception and wire it into `withdraw`.
4. Write `save_accounts`/`load_accounts` and test them independently —
   save two accounts, restart your program, load them back.
5. Only then build the interactive menu loop in `main.py`.

## Stretch Goals (optional)
- Apply `interest_rate` to all accounts with a `apply_interest()` class method.
- Keep a transaction history (list of strings) per account.
- Use `json` instead of plain text for storage (more robust for special characters).

## Testing Checklist
- [ ] Withdrawing more than the balance raises `InsufficientFundsError`, doesn't crash
- [ ] Depositing a negative number is rejected
- [ ] A failed transfer doesn't deduct money from the sender
- [ ] Saving then loading gives back the same balances
- [ ] Loading when no save file exists doesn't crash (starts with empty list)
