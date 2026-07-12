# Input
weight = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

# Convert height to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Output
print("BMI:", round(bmi, 1))