# Taxi Fare Calculator

print("===== Taxi Fare Calculator =====")

num_trips = int(input("Enter number of trips: "))

for i in range(num_trips):
    print(f"\nEnter details for trip {i + 1}:")

    distance = float(input("Distance traveled (km): "))
    hour = int(input("Travel hour (0-23): "))

    # Calculate fare
    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + (distance - 2) * 35
    else:
        fare = 150 + (8 * 35) + (distance - 10) * 28

    # Apply night surcharge (10 PM to 5 AM)
    if hour >= 22 or hour < 5:
        fare += fare * 0.10
        surcharge = "Yes"
    else:
        surcharge = "No"

    print("\n===== Fare Details =====")
    print(f"Distance: {distance} km")
    print(f"Travel Time: {hour}:00")
    print(f"Night Surcharge Applied: {surcharge}")
    print(f"Total Fare: NPR {fare:.2f}")