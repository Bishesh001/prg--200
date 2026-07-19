# Inventory Restock Alert - Interactive Version

inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

print("===== Grocery Store Inventory Restock System =====")

# Let user update stock for each item
for product in inventory:
    print(f"\nCurrent item: {product['item']}")
    print(f"Previous stock: {product['stock']}")
    
    new_stock = int(input(f"Enter updated stock for {product['item']}: "))
    product["stock"] = new_stock

# Check inventory for restocking
restock_count = 0

print("\n===== Inventory Restock Check =====")

for product in inventory:
    print(f"\nChecking {product['item']}...")
    print(f"Current Stock: {product['stock']}")
    print(f"Threshold Level: {product['threshold']}")

    if product["stock"] < product["threshold"]:
        print(f"Restock Alert: {product['item']} needs restocking!")
        restock_count += 1
    else:
        print(f"{product['item']} has sufficient stock.")

# Final summary
print("\n===== Inventory Summary =====")
print(f"Total items that need restocking: {restock_count}")