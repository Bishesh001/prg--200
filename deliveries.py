deliveries = [
    ("Order1", 45),
    ("Order2", 20),
    ("Order3", 30),
    ("Order4", 15)
]

deliveries.sort(key=lambda x: x[1])

print(deliveries)