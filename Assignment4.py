class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []  # list of (seat_number, passenger_name)

    def book_seat(self, seat_number, passenger_name):
        for seat, _ in self.booked:
            if seat == seat_number:
                print("Seat already booked")
                return
        self.booked.append((seat_number, passenger_name))

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print(f"Passenger list for {self.route}:")
        for seat, name in self.booked:
            print(f"Seat {seat}: {name}")


route = input("Enter bus route (e.g. Kathmandu - Pokhara): ")
total_seats = int(input("Enter total number of seats: "))
bus = Bus(route, total_seats)

while True:
    print("\n1. Book a seat  2. Show available seats  3. Show passenger list  4. Exit")
    option = input("Choose an option: ")

    if option == "1":
        seat_number = int(input("Enter seat number: "))
        passenger_name = input("Enter passenger name: ")
        bus.book_seat(seat_number, passenger_name)

    elif option == "2":
        print(f"Available seats: {bus.available_seats()}")

    elif option == "3":
        bus.passenger_list()

    elif option == "4":
        break

    else:
        print("Invalid option")