# learning atms logic

accounts = {
    "1001": {"name": "Bishesh", "pin": "1234", "balance": 5000},
    "1002": {"name": "Ram Sharma", "pin": "5678", "balance": 10000}
}

print("Welcome to Nepal Bank Limited ATM")

acc_no = input("Enter your account number: ")

if acc_no not in accounts:
    print("Invalid account number, please try again")

else:
    account = accounts[acc_no]  # FIX: was "accounts" typo

    entered_pin = input("Enter your pin: ")

    if entered_pin != account["pin"]:  # FIX: check wrong pin first
        print("Invalid pin")

    else:
        print("My master welcome", account["name"])

        while True:  # FIX: True not true
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose: ")

            if choice == "1":
                print("Balance: Rs", account["balance"])

            elif choice == "2":
                amount = int(input("Enter deposit amount: "))
                account["balance"] = account["balance"] + amount
                print("Deposited! New balance: Rs", account["balance"])

            elif choice == "3":
                amount = int(input("Enter withdraw amount: "))
                if amount > account["balance"]:
                    print("Not enough money!")
                else:
                    account["balance"] = account["balance"] - amount
                    print("Withdrawn! Remaining: Rs", account["balance"])

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")