# Input
trekkers = int(input("Enter the number of trekkers: "))
fee_per_person = float(input("Enter TIMS + ACAP fee per person: "))

# Calculate total fee
total_fee = trekkers * fee_per_person

# Add 5% agency service charge
total_cost = total_fee + (0.05 * total_fee)

# Calculate average cost per person
average_cost = total_cost / trekkers

# Output
print("Total cost for the group:", total_cost)
print("Average cost per person:", average_cost)