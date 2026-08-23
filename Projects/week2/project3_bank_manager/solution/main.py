"""
main.py - Interactive menu for the Bank Account Manager.
Part of Project 3: Bank Account Manager (SOLUTION)
"""

from account import Account, InsufficientFundsError, transfer
from storage import save_accounts, load_accounts

MENU_TEXT = """
==== Bank Account Manager ====
1. Create account
2. Deposit
3. Withdraw
4. Transfer
5. View all accounts
6. Save & Quit
"""


def find_account(accounts, owner):
    for acc in accounts:
        if acc.owner.lower() == owner.lower():
            return acc
    return None


def main():
    accounts = load_accounts()

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            owner = input("Account owner name: ").strip()
            if find_account(accounts, owner):
                print("An account with that name already exists.")
                continue
            try:
                starting_balance = float(input("Starting balance: ") or 0)
                accounts.append(Account(owner, starting_balance))
                print(f"Created account for {owner}.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            acc = find_account(accounts, input("Owner name: "))
            if not acc:
                print("Account not found.")
                continue
            try:
                amount = float(input("Deposit amount: "))
                acc.deposit(amount)
                print(f"New balance: ${acc.balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            acc = find_account(accounts, input("Owner name: "))
            if not acc:
                print("Account not found.")
                continue
            try:
                amount = float(input("Withdraw amount: "))
                acc.withdraw(amount)
                print(f"New balance: ${acc.balance:.2f}")
            except (ValueError, InsufficientFundsError) as e:
                print(f"Error: {e}")

        elif choice == "4":
            sender = find_account(accounts, input("From (owner name): "))
            receiver = find_account(accounts, input("To (owner name): "))
            if not sender or not receiver:
                print("One or both accounts not found.")
                continue
            try:
                amount = float(input("Transfer amount: "))
                transfer(sender, receiver, amount)
                print(f"Transferred ${amount:.2f} from {sender.owner} to {receiver.owner}.")
            except (ValueError, InsufficientFundsError) as e:
                print(f"Transfer failed: {e}")

        elif choice == "5":
            if not accounts:
                print("No accounts yet.")
            for acc in accounts:
                print(acc)  # uses Account.__str__

        elif choice == "6":
            save_accounts(accounts)
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-6.")


if __name__ == "__main__":
    main()
