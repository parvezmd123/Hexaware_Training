import csv

with open("employees.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)


#Skip header
print("\nSkipping header:\n")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)   # Skip header
    for row in reader:
        print(row)


# Print Employee Names
print("\nEmployee Names:\n")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])


# Count number of Employees
count = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count += 1
print("\nTotal Employees:", count)


# Exercise 4
# Find highest salary.

highest_salary = 0
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        if salary > highest_salary:
            highest_salary = salary

print("\nHighest Salary:", highest_salary)


# Exercise 5
# Find lowest salary.

lowest_salary = float('inf')
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        if salary < lowest_salary:
            lowest_salary = salary
print("\nLowest Salary:", lowest_salary)

# Exercise 6
# Find average salary.

total_salary = 0
employee_count = 0
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        total_salary += salary
        employee_count += 1

if employee_count > 0:
    average_salary = total_salary / employee_count
else:
    average_salary = 0
print("\nAverage Salary:", average_salary)


# Exercise 7
# Find total salary payout.

total_salary_payout = 0
with open("employees.csv","r") as file: 
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        total_salary_payout += salary
print("\nTotal Salary Payout:", total_salary_payout)

# Exercise 8
# Display Hyderabad employees.


print("\nHyderabad Employees:\n")
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[4] == "Hyderabad":
            print(row)



# Exercise 9
# Display AI Engineering employees.

print("\nAI Engineering Employees:\n")
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[2] == "AI Engineering":
            print(row)  


# Exercise 10
# Display employees earning above ₹80,000.

print("\nEmployees earning above ₹80,000:\n")
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        if salary > 80000:
            print(row)
