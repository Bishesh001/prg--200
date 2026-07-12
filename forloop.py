mark_list = []
Name_list = []

for i in range(20):
    mark = float(input("Enter the marks of the student: "))
    name = input("Enter the name of the student: ")

    mark_list.append(mark)
    Name_list.append(name)

print("\nFinal Result")

for i in range(20):
    if mark_list[i] >= 90:
        grade = "A"
    elif mark_list[i] >= 80:
        grade = "B"
    elif mark_list[i] >= 70:
        grade = "C"
    elif mark_list[i] >= 60:
        grade = "D"
    else:
        grade = "F"

    print(Name_list[i], "-", mark_list[i], "-", grade)