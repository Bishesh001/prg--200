class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        status = "Pass" if avg >= 40 else "Fail"
        print(f"{self.name}: Average = {avg:.2f}, Grade = {self.grade()}, {status}")


students = []

num_students = int(input("How many students do you want to enter? "))
for i in range(num_students):
    print(f"\nStudent {i + 1}:")
    name = input("Enter name: ")
    marks = []
    for subject in range(1, 6):
        mark = float(input(f"Enter marks for subject {subject}: "))
        marks.append(mark)
    students.append(Student(name, marks))

print("\n--- Report Cards ---")
for student in students:
    student.display()