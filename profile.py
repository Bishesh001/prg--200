def build_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key + ":", value)


build_profile(
    "Bishesh",
    age=21,
    course="PRG-300",
    city="Kathmandu",
    hobby="Coding"
)