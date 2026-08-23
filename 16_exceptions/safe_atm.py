class InvalidAmountError(Exception):
    pass

balance = 1000

try:
    amount = float(input("Withdrawal amount: "))

    if amount <= 0:
        raise InvalidAmountError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")

except ValueError as error:
    print("Value error:", error)
except InvalidAmountError as error:
    print("Custom error:", error)
else:
    balance -= amount
    print("Withdrawal successful. New balance:", balance)
finally:
    print("ATM session finished.")
