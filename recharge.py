def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 150
    elif gb == 2:
        price = 250
    elif gb == 5:
        price = 500
    elif gb == 10:
        price = 900
    else:
        return "Invalid data pack"

    return price


gb = int(input("Enter data pack (GB): "))

cost = recharge_cost(gb)

print("Price: Rs.", cost)
print("Validity:", 30, "days")