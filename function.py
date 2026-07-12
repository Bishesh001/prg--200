# USD to NPR Converter (loop version, no custom functions)

rate = 152.50  # 1 USD = 152.50 NPR (approx.)

while True:
    usd = input("Enter amount in USD (or type 'stop' to quit): ")

    if usd == "stop":
        print("Program stopped. Goodbye!")
        break

    usd = float(usd)
    npr = usd * rate
    print("USD", usd, "=", "NPR", npr)
    print()