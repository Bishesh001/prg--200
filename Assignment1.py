class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"{self.name} ({self.account_number}): NPR {self.balance}")


accounts = {}

num_accounts = int(input("How many accounts do you want to create? "))
for i in range(num_accounts):
    print(f"\nAccount {i + 1}:")
    name = input("Enter name: ")
    acc_no = input("Enter account number: ")
    balance = float(input("Enter starting balance: "))
    accounts[acc_no] = BankAccount(name, acc_no, balance)

while True:
    print("\n1. Deposit  2. Withdraw  3. Check balance  4. Show all accounts  5. Exit")
    option = input("Choose an option: ")

    if option == "1":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amt = float(input("Amount to deposit: "))
            accounts[acc_no].deposit(amt)
        else:
            print("Account not found")

    elif option == "2":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amt = float(input("Amount to withdraw: "))
            accounts[acc_no].withdraw(amt)
        else:
            print("Account not found")

    elif option == "3":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            accounts[acc_no].get_balance()
        else:
            print("Account not found")

    elif option == "4":
        for account in accounts.values():
            account.get_balance()

    elif option == "5":
        break

    else:
        print("Invalid option")