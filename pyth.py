def  add(a, b):
    sum = (a + b)
    return (sum)

total= add(3, 4)
print (total)
def ticket_price(seat_type):
    if seat_type == "regular":
        return 500
    elif seat_type == "recliner":
        return 800
    else:
        return 0


seat = input("Enter seat type (regular/recliner): ").lower()

price = ticket_price(seat)

if price == 0:
    print("Invalid seat type")
else:
    print("Ticket Price: Rs.", price)