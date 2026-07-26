# Question 1 - Small Shop Billing and Inventory System
# ======================================================
 
# given data
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}
 
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
 
 
def process_order(inventory, cart):
    # this will hold each line of the bill so we can print it at the end
    bill_lines = []
    grand_total = 0
 
    # go through every item the customer wants to buy
    for item, qty in cart.items():
        available_stock = inventory[item]["stock"]
 
        # if there isn't enough stock, skip the item and tell the shopkeeper
        if qty > available_stock:
            print(f"Sorry, not enough stock for {item}")
            continue
 
        # enough stock is available, so calculate the cost of this item
        price = inventory[item]["price"]
        item_total = price * qty
 
        # add to the bill and the grand total
        bill_lines.append(f"{item} x{qty} = NPR {item_total}")
        grand_total += item_total
 
        # reduce the stock since these items are now sold
        inventory[item]["stock"] -= qty
 
    # print the final bill
    print("---- Bill ----")
    for line in bill_lines:
        print(line)
    print(f"Grand Total: NPR {grand_total}")
    print("--------------")
 
    # print the stock left after this purchase
    updated_stock = ", ".join(f"{item}={data['stock']}" for item, data in inventory.items())
    print(f"Updated stock: {updated_stock}")
 
 
print("QUESTION 1")
 
# build the cart from what the user types in, instead of using the fixed one above
user_cart = {}
print("Enter items to buy (type 'done' when finished)")
print(f"Available items: {', '.join(inventory.keys())}")
 
while True:
    item_name = input("Item name: ").strip().lower()
 
    if item_name == "done":
        break
 
    if item_name not in inventory:
        print("That item is not in the shop, try again")
        continue
 
    qty = int(input(f"Quantity of {item_name}: "))
    user_cart[item_name] = qty
 
process_order(inventory, user_cart)
print()
 