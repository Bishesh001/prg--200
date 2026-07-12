# Input
previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
rate_per_unit = float(input("Enter rate per unit: "))
service_charge = float(input("Enter monthly service charge: "))

# Calculate units consumed
units = current_reading - previous_reading

# Basic bill amount
bill = units * rate_per_unit

# Extra charge after 50 units
if units > 50:
    extra_charge = bill * 0.10   # 10% extra charge
else:
    extra_charge = 0

# Total bill
total_bill = bill + extra_charge + service_charge

# Output
print("Units Consumed:", units)
print("Basic Bill:", bill)
print("Extra Charge:", extra_charge)
print("Service Charge:", service_charge)
print("Total Electricity Bill:", total_bill)