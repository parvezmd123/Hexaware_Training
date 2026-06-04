#List
cities = ["Hyderabad", "Mumbai", "Delhi"]

print(cities[0])
print(cities[1])
print(cities[2])

# Negative Indexing
print(cities[-1])
print(cities[-2])

# Update an Element
cities[1] = "Bangalore"
print(cities)

# Append
cities.append("Chennai")
print(cities)

# Insert
cities.insert(1, "Salem")
print(cities)

# Multiple Values
cities.extend(["Kochi", "Pondi"])
print(cities)

# Remove
cities.remove("Chennai")
print(cities)

cities.pop(1)
print(cities)

del cities[4]
print(cities)

cities.clear()
print(cities)

print(len(cities))

cities = ["Hyderabad", "Mumbai", "Delhi"]

print('Delhi' in cities)
print('Chennai' in cities)

print(cities.index('Mumbai'))

l = sorted(cities)
print(l)

cities = ("Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune")
print(cities)

print(cities[0])
print(cities[1])

print(cities[-1])
print(cities[-2])

print(len(cities))

print(cities[1:4])

cities[1] = "Bangalore"

employee = (101, "Rahul", "IT", 75000)

eid, name, dept, sal = employee

print(eid)
print(name)
print(sal)


def get_employee():
    return 102, "Rahul", "IT", 75000


res = get_employee()
print(res)

cities = {"Hyderabad", "Mumbai", "Delhi", "Mumbai"}
print(cities)

cities.add('Chennai')
print(cities)

cities.update(["Delhi", 'Pune'])
print(cities)

cities.remove("Mumbai")
print(cities)

cities.discard("Mumbai")  # No error raises if item not in set
print(cities)

set1 = {"Python", "SQL"}
set2 = {"MongoDB", "Python"}

# union() -> Combines all unique elements
result = set1.union(set2)
print(result)

# intersection() -> Common elements
result = set1.intersection(set2)
print(result)

# difference() -> Elements present only in set1
result = set1.difference(set2)
print(result)

# symmetric_difference() -> Non-common elements
result = set1.symmetric_difference(set2)
print(result)

customer = {
    "customer_id": 101,
    "name": "Rahul",
    "city": "Hyderabad"
}  # Dictionary

print(customer)

print(customer["name"])
print(customer["city"])

# safe
print(customer.get("name"))
print(customer.get("salary"))

# Add New Key Value Pair
customer["salary"] = 75000
print(customer)

# Update
customer["name"] = "Rahul Sharma"
print(customer)

customer.pop("salary")
print(customer)

del customer["city"]

print(customer)
