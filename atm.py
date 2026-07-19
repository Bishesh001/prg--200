# Week 3 - Question 1: ATM Withdrawal Validator
# A Nepali bank ATM checks three rules before allowing a withdrawal:
#   1. The amount must be a multiple of NPR 500
#   2. The amount must not be more than the account balance
#   3. Total withdrawn today (including this withdrawal) cannot cross NPR 50,000

DAILY_LIMIT = 50000

# Pre-given account (like the ATM already knows whose card is inserted)
account_number = "1234"
balance = 25000
daily_withdrawn = 0


def process_withdrawal(balance, daily_withdrawn, amount):
    # Checks all the rules one by one and prints the correct message.
    # Returns the updated balance (unchanged if the withdrawal failed).

    if amount % 500 != 0:
        print("Invalid amount. Must be a multiple of NPR 500.")
    elif daily_withdrawn + amount > DAILY_LIMIT:
        print("Daily withdrawal limit reached.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        print("Withdrawal successful.")
        print(f"Your current balance after withdrawal: NPR {balance}")

    return balance


# Show which account is being used, then take the withdrawal amount
print(f"Account Number: {account_number}")
print(f"Current Balance: NPR {balance}")
print(f"Already Withdrawn Today: NPR {daily_withdrawn}")

amount = float(input("Enter amount to withdraw: "))

balance = process_withdrawal(balance, daily_withdrawn, amount)