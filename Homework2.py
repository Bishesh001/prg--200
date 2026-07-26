sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]
 
 
def check_water_level(location, level_metres):
    # decide the alert level based on the water height
    if level_metres < 3:
        return "Safe"
    elif level_metres <= 5:
        return "Warning - Alert nearby villages"
    else:
        return "DANGER - Evacuate immediately!"
 
 
print("QUESTION 2")
 
# still checks the given sensors first
for location, level in sensors:
    status = check_water_level(location, level)
    print(f"{location} ({level} m): {status}")
 
# then lets the user check their own reading too
print("\nEnter a reading to check (type 'done' when finished)")
while True:
    user_location = input("Location name: ").strip()
 
    if user_location.lower() == "done":
        break
    user_level = float(input("Water level in metres: "))
    status = check_water_level(user_location, user_level)
    print(f"{user_location} ({user_level} m): {status}")
print()
 
 