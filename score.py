def average_score(*marks):
    total = sum(marks)
    average = total / len(marks)
    return average


print("Average:", average_score(80, 90, 70))
print("Average:", average_score(85, 90, 75, 80, 95))