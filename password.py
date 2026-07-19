# Password Strength Checker

print("===== Password Strength Checker =====")

num_passwords = int(input("How many passwords do you want to check? "))

passwords = []

for i in range(num_passwords):
    password = input(f"Enter password {i + 1}: ")
    passwords.append(password)

special_chars = "!@#$%^&*"

for password in passwords:
    print(f"\nChecking password: {password}")

    missing = []

    if len(password) < 8:
        missing.append("At least 8 characters long")

    if not any(char.isupper() for char in password):
        missing.append("At least one uppercase letter")

    if not any(char.islower() for char in password):
        missing.append("At least one lowercase letter")

    if not any(char.isdigit() for char in password):
        missing.append("At least one digit")

    if not any(char in special_chars for char in password):
        missing.append("At least one special character (!@#$%^&*)")

    if not missing:
        print("Strong password.")
    else:
        print("Weak password. Missing:")
        for item in missing:
            print("-", item)