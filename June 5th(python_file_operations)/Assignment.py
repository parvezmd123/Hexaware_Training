with open("employees.txt","r") as file:
    employees=[line.strip().split(",") for line in file]

#Exercise 1
with open("employees.txt","r") as file:
    print(file.read())

#2
with open("employees.txt","r") as file:
    for line in file:
        print(line.strip())

#3
print("Total employees=",len(employees))

#4
for emp in employees:
    print(emp[1])

#5
for emp in employees:
    if emp[4]==("Hyderabad"):
        print(emp)

#6
for emp in employees:
    if emp[4]==("Bangalore"):
        print(emp)

#7
# for emp in employees:
#     if (emp[3]) >80000:
#         print(emp)

#8
highest_salary=max(int(emp[3]) for emp in employees)
print(highest_salary)

#9
lowest_salary=min(int(emp[3]) for emp in employees)
print(lowest_salary)

#10
average_salary=sum(int(emp[3]) for emp in employees)/len(employees)
print(average_salary)

#11
total_salary=sum(int(emp[3]) for emp in employees)
print(total_salary)

# Exercise 12
ai_count = sum(1 for emp in employees if emp[2] == "AI Engineering")
print("AI Engineering =", ai_count)

# Exercise 13
de_count = sum(1 for emp in employees if emp[2] == "Data Engineering")
print("Data Engineering =", de_count)

# Exercise 14
for emp in employees:
    if emp[2] == "AI Engineering":
        print(emp)

# Exercise 15
with open("high_salary_employees.txt", "w") as file:
    for emp in employees:
        if int(emp[3]) > 80000:
            file.write(",".join(emp) + "\n")
print("high_salary_employees.txt created")

# Exercise 16
with open("hyderabad_employees.txt", "w") as file:
    for emp in employees:
        if emp[4] == "Hyderabad":
            file.write(",".join(emp) + "\n")
print("hyderabad_employees.txt created")

# Exercise 17
cities = set(emp[4] for emp in employees)
for city in cities:
    print(city)
print("Unique Cities =", len(cities))

# Exercise 18
dept_count = {}
for emp in employees:
    dept = emp[2]
    dept_count[dept] = dept_count.get(dept, 0) + 1

for dept, count in dept_count.items():
    print(dept, "=", count)

# Exercise 19
highest_paid = max(employees, key=lambda x: int(x[3]))
print(highest_paid[1])
print(highest_paid[3])

# Exercise 20
with open("employee_report.txt", "w") as file:
    file.write(f"Total Employees: {len(employees)}\n")
    file.write(f"Highest Salary: {highest_salary}\n")
    file.write(f"Lowest Salary: {lowest_salary}\n")
    file.write(f"Average Salary: {average_salary}\n")
    file.write(f"Total Salary: {total_salary}\n")

print("employee_report.txt created")
