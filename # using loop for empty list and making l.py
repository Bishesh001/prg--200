#  using loop for empty list  and making loopinga and asking input from user
mark_list = []

for i in range(20):
    mark = int(input("enter mark: "))
    mark_list.append(mark)
for mark in mark_list:
    if mark >= 90:
        print(f"{mark} is an A grade")
    elif mark >= 80:
        print(f"{mark} is a B grade")
    elif mark >= 70:
        print(f"{mark} is a C grade")
    elif mark >= 60:
        print(f"{mark} is a D grade")
    else:
        print(f"{mark} is an F grade")