#Exception Handling
from unittest import result
try:
    a=10
    b=0
    result=a/b
    print(result)
except:
    print("Error Occured")
print("Program completed")

#Specific Exception
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#Another Exception
try:
    age=int(input("Enter age:"))
    print(age)
except ValueError:
    print("Please enter a Numeric value")


try:
    age=int(input("Enter age:"))
    print(100/age)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Age cannot be Zero")

#Exception Object


try:
    print(10/0)
except:
    print("Error")

finally:
    print("Connection Closed")

#Raise Error
salary=-1000

if salary<0:
    raise ValueError(
        "Salary cannot be negative"
    )

#File operations

file = open("employees.txt", "r")
data = file.read()
print(data)
file.close()

#read single line
file = open("employees.txt", "r")
print(file.readline())
file.close()

#multiple lines
file = open("employees.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#Automatic closing
with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

# #write to file - overwrites existing content
with open("employees1.txt","w")as file:
    file.write("John - Manager\n")
    file.write("Sara - Developer\n")
    file.write("Mike - Designer\n")


# #append to file - adds to existing content
with open("employees1.txt","a")as file:
    file.write("Emily - Analyst\n")
    file.write("David - Tester\n")
