# Input
basic_salary = float(input("Enter your monthly basic salary: "))
tax_percent = float(input("Enter the tax percentage: "))

# Salary + Dashain bonus
gross_amount = basic_salary * 2

# Tax deduction
tax = (gross_amount * tax_percent) / 100

# Final take-home amount
take_home = gross_amount - tax

# Output
print("Monthly Salary:", basic_salary)
print("Dashain Bonus:", basic_salary)
print("Gross Amount:", gross_amount)
print("Tax Deduction:", tax)
print("Final Take-Home Amount:", take_home)