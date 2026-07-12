
def calculate_fare(distance, vehicle_type, surge=1):

    if vehicle_type == "bike":
        rate = 20
    elif vehicle_type == "car":
        rate = 40
    else:
        return "Invalid vehicle type"

    fare = distance * rate * surge
    return fare


distance = float(input("Enter distance (km): "))
vehicle = input("Enter vehicle type (bike/car): ").lower()

price = calculate_fare(distance, vehicle)

print("Estimated Fare: Rs.", price)