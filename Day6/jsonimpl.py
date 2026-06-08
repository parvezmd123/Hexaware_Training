import json

employees = [

    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },

    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },

    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },

    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },

    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }

]

with open("employees.json", "w") as file:
  json.dump(employees,file, indent=4 )

print("employees.json file created")


import json

from annotated_types import Len


with open("employees.json", "r") as file:
  data = json.load(file)
  
print(data)


for employee in data:
  print(employee)

for employee in data:
  print(employee["name"]) # Print names

print("Length:" ,Len(data)) # Find number of Employees

# Highest Salary
highest_salary = 0

for employee in data:

  if employee["salary"] > highest_salary:
    highest_salary = employee["salary"]

print("Highest Salary: ", highest_salary)


# Find Average Salary

total_salary = 0

for employee in data:
  total_salary += employee["salary"]
average_salary = total_salary / len(data)
print("Average Salary: ", average_salary)



# Display Data Engineering Employees

for employee in data:
  if employee["department"] == "Data Engineering":
    print(employee)


# Display Employees Earning More Than 80000

for employee in data:
  if employee["salary"]>80000:
    print(employee["name"], employee["salary"])

# Update Salary of one of employees
for employee in data:
  if employee["employee_id"] == 105:
    employee["salary"] = 100000
    print(employee["name"], "Salary Updated to: ", employee["salary"])
                   
# Add New Employee

new_employee = {
    "employee_id": 108,
    "name": "Kiran",
    "department": "AI Engineering",
    "salary": 88000,
    "city": "Pune"
}

data.append(new_employee)

# Delete an Employee

for employee in data:
  if employee["employee_id"] == 103:
    data.remove(employee)
    print(employee["name"], "has been removed from the records")

# Save Updated Data to JSON File
with open("employees.json", "w") as file:
  json.dump(data, file, indent=4)
