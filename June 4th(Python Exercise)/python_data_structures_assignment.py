# ==========================
# Dataset 1: Employee Salaries (List)
# ==========================

salaries = [45000, 55000, 65000, 75000, 85000]

# Exercise 1
print("All Salaries:", salaries)

# Exercise 2
print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))

# Exercise 3
print("Total Salary Payout:", sum(salaries))

# Exercise 4
print("Average Salary:", sum(salaries) / len(salaries))

# Exercise 5
salaries.append(95000)
salaries.append(105000)
print("After Adding Salaries:", salaries)

# Exercise 6
salaries.remove(55000)
print("After Removing 55000:", salaries)

# Exercise 7
print("Ascending Order:", sorted(salaries))

# Exercise 8
print("Descending Order:", sorted(salaries, reverse=True))

# Exercise 9
sorted_salaries = sorted(salaries, reverse=True)
print("Second Highest Salary:", sorted_salaries[1])

# Exercise 10
print("Salaries Greater Than 70000:")
for salary in salaries:
    if salary > 70000:
        print(salary)


# ==========================
# Dataset 2: Employee Record (Tuple)
# ==========================

employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)

# Exercise 11
print("\nAll Tuple Values:", employee)

# Exercise 12
print("Employee Name:", employee[1])

# Exercise 13
print("Department:", employee[2])

# Exercise 14
emp_id, name, department, salary = employee
print("Unpacked Values:")
print(emp_id, name, department, salary)

# Exercise 15
print("Length:", len(employee))
print("First Element:", employee[0])
print("Last Element:", employee[-1])


# ==========================
# Dataset 3: Batch Students (Set)
# ==========================

batch_a = {"Rahul", "Priya", "Amit", "Sneha", "Farhan"}
batch_b = {"Priya", "Sneha", "Neha", "Arjun", "Farhan"}

# Exercise 16
print("\nCommon Students:", batch_a.intersection(batch_b))

# Exercise 17
print("Only in Batch A:", batch_a.difference(batch_b))

# Exercise 18
print("Only in Batch B:", batch_b.difference(batch_a))

# Exercise 19
print("All Unique Students:", batch_a.union(batch_b))

# Exercise 20
print("Present in One Batch but Not Both:",
      batch_a.symmetric_difference(batch_b))


# ==========================
# Dataset 4: Employee Dictionary
# ==========================

employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

# Exercise 21
print("\nEmployee Name:", employee_info["name"])

# Exercise 22
print("Department:", employee_info["department"])
print("City:", employee_info["city"])

# Exercise 23
employee_info["experience"] = 5
print("After Adding Experience:", employee_info)

# Exercise 24
employee_info["salary"] = 85000
print("After Updating Salary:", employee_info)

# Exercise 25
employee_info.pop("city")
print("After Removing City:", employee_info)

# Exercise 26
print("Keys:", employee_info.keys())

# Exercise 27
print("Values:", employee_info.values())

# Exercise 28
print("Key-Value Pairs:")
for key, value in employee_info.items():
    print(key, ":", value)


# ==========================
# Dataset 5: List of Dictionaries
# ==========================

employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    {"id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]

# Exercise 29
print("\nEmployee Names:")
for emp in employees:
    print(emp["name"])

# Exercise 30
print("\nIT Department Employees:")
for emp in employees:
    if emp["department"] == "IT":
        print(emp)

# Exercise 31
highest_salary_emp = max(employees, key=lambda x: x["salary"])
print("\nHighest Salary Employee:", highest_salary_emp)

# Exercise 32
lowest_salary_emp = min(employees, key=lambda x: x["salary"])
print("Lowest Salary Employee:", lowest_salary_emp)

# Exercise 33
avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average Salary:", avg_salary)

# Exercise 34
total_salary = sum(emp["salary"] for emp in employees)
print("Total Salary Payout:", total_salary)

# Exercise 35
print("\nEmployees Earning More Than 70000:")
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)

# Exercise 36
it_count = sum(1 for emp in employees if emp["department"] == "IT")
print("Number of IT Employees:", it_count)

# Exercise 37
sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print("\nEmployee Names Sorted by Salary Descending:")
for emp in sorted_employees:
    print(emp["name"], "-", emp["salary"])

# Exercise 38
second_highest = sorted_employees[1]
print("Second Highest Salary Employee:", second_highest)

# Exercise 39
departments = {emp["department"] for emp in employees}
print("Departments Without Duplicates:", departments)
