class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        return 0  # overridden by child classes

    def display(self):
        print(f"{self.name} ({self.partner_id}) - Deliveries: {self.deliveries}, "
              f"Total Earning: NPR {self.total_earning()}")


class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        return (self.deliveries * 80) + (self.km_travelled * 5)


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        return (self.deliveries * 60) + (self.rainy_deliveries * 50)


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        return (self.deliveries * 120) - self.fuel_cost


partners = []

num_partners = int(input("How many delivery partners do you want to enter? "))
for i in range(num_partners):
    print(f"\nPartner {i + 1}:")
    print("1. Bike Rider  2. Walker  3. Car Driver")
    kind = input("Choose type: ")
    name = input("Name: ")
    pid = input("Partner ID: ")
    deliveries = int(input("Number of deliveries: "))

    if kind == "1":
        km = float(input("KM travelled: "))
        partners.append(BikeRider(name, pid, deliveries, km))
    elif kind == "2":
        rainy = int(input("Rainy deliveries: "))
        partners.append(Walker(name, pid, deliveries, rainy))
    elif kind == "3":
        fuel = float(input("Fuel cost: "))
        partners.append(CarDriver(name, pid, deliveries, fuel))
    else:
        print("Invalid type, skipping this partner")

print("\n--- Delivery Partner Earnings ---")
for partner in partners:
    partner.display()

if partners:
    top_earner = max(partners, key=lambda p: p.total_earning())
    print(f"\nHighest earner: {top_earner.name} with NPR {top_earner.total_earning()}")