floors = 10
count = 1

while count <= floors:
    print("\nFloor", count)

    shop = input("Enter shop name: ")
    units = int(input("Enter electricity units: "))

    if units <= 30:
        rate = 10
    elif units <= 50:
        rate = 12
    elif units <= 70:
        rate = 14
    elif units <= 100:
        rate = 16
    else:
        rate = 20

    bill = units * rate

    print("Shop Name:", shop)
    print("Units:", units)
    print("Rate: Rs", rate, "per unit")
    print("Bill: Rs", bill)

    count = count + 1