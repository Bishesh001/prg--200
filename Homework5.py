# Question 5 - Simple ATM Simulator
# ======================================================
 
accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"}
}
 
 
def atm(account_id, pin, action, amount=0):
    # check the account exists first
    if account_id not in accounts:
        print("Account not found")
        return
 
    account = accounts[account_id]
 
    # check the pin matches before doing anything else
    if account["pin"] != pin:
        print("Incorrect PIN")
        return
 
    if action == "balance":
        print(f'{account["name"]} - Current Balance: NPR {account["balance"]}')
 
    elif action == "deposit":
        account["balance"] += amount
        print(f'Deposit successful. New balance: NPR {account["balance"]}')
 
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f'Withdrawal successful. New balance: NPR {account["balance"]}')
 
 
print("QUESTION 5")
 
# use the ATM
print("Use the ATM (type 'done' as the account ID to stop)")
while True:
    user_account = input("Account ID: ").strip().upper()
 
    if user_account == "DONE":
        break
 
    user_pin = input("PIN: ").strip()
    user_action = input("Action (balance/deposit/withdraw): ").strip().lower()
 
    user_amount = 0
    if user_action in ("deposit", "withdraw"):
        user_amount = int(input("Amount: "))
 
    atm(user_account, user_pin, user_action, user_amount)