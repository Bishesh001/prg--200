# Online Store Discount System

print("===== Online Store Discount System =====")

purchase_amount = float(input("Enter total purchase amount (NPR): "))
loyalty_member = input("Are you a loyalty member? (yes/no): ").strip().lower()

# Determine discount rate
if purchase_amount < 1000:
    discount_rate = 0
elif purchase_amount < 5000:
    discount_rate = 0.05
elif purchase_amount < 15000:
    discount_rate = 0.10
else:
    discount_rate = 0.20

# Apply purchase discount
discounted_amount = purchase_amount - (purchase_amount * discount_rate)

# Apply loyalty discount
if loyalty_member == "yes":
    discounted_amount -= discounted_amount * 0.05

print(f"Original Amount: NPR {purchase_amount:.2f}")
print(f"Purchase Discount: {discount_rate * 100:.0f}%")

if loyalty_member == "yes":
    print("Loyalty Discount: 5% applied")

print(f"Final Payable Amount: NPR {discounted_amount:.2f}")