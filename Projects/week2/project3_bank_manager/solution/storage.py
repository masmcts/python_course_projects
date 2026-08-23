"""
storage.py - Save/load accounts to a text file.
Part of Project 3: Bank Account Manager (SOLUTION)
"""

from account import Account


def save_accounts(accounts, filename="accounts.txt"):
    """Write each account as 'owner,balance' on its own line."""
    with open(filename, "w") as f:
        for acc in accounts:
            f.write(f"{acc.owner},{acc.balance:.2f}\n")
    print(f"Saved {len(accounts)} account(s) to {filename}.")


def load_accounts(filename="accounts.txt"):
    """Read accounts back from a file. Returns [] if the file doesn't exist."""
    accounts = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                owner, balance = line.split(",")
                accounts.append(Account(owner, float(balance)))
    except FileNotFoundError:
        print(f"No existing save file '{filename}' found — starting fresh.")
    return accounts
