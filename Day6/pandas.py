import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr*2)
print(arr+5)
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.std())
print(arr.var())
print(arr.shape)
print(arr[0])
print(arr[1:4])
print(arr[arr>3])
print(arr[arr%2==0])



#2D Array
print("\n2D Array:")
arr2 = np.array([[10, 20, 30], 
                 [40, 50, 60]])
print(arr2)
print(arr2*2)
print(arr2+5)
print(arr2.sum())
print(arr2.mean())
print(arr2.max())
print(arr2.min())
print(arr2.std())
print(arr2.var())
print(arr2.shape)
print(arr2[0, 1])# Access element at row 0 and column 1
print(arr2[1, :])# Access all elements in row 1
print(arr2[:, 2])# Access all elements in column 2
print(arr2[arr2>30])# Access elements greater than 30
print(arr2[arr2%20==0])# Access elements divisible by 20
print(arr2.T) # Transpose of the array
print(arr2.flatten()) # Flatten the array to 1D
print(arr2.reshape(3, 2)) # Reshape the array to 3 rows and 2 columns
print(arr2.reshape(6)) # Reshape the array to 1D with 6 elements
print(arr2.reshape(2, -1)) # Reshape the array to 2 rows and automatically determine the number of columns


import numpy as np

arr = np.zeros(10)
print(arr)# Create an array of zeros with 10 elements

arr = np.ones(5)
print(arr) # Create an array of ones with 5 elements

arr = np.arange(1, 11)
print(arr) # Create an array of integers from 1 to 10

arr = np.linspace(10, 100, 5)
print(arr) # Create an array of 5 evenly spaced numbers between 10 and 100

arr = np.random.rand(3, 3)
print(arr) # Create a 3x3 array of random numbers between 0 and 1



######################################PANDAS######################################

data = {

    "employee_id": [101,102,103],

    "name": [
        "Rahul",
        "Priya",
        "Amit"
    ],

    "salary": [
        75000,
        85000,
        65000
    ]
}
print(data)
df = pd.DataFrame(data)
print(df)
print(df["name"]) # Access the 'name' column
print(df["salary"].mean()) # Calculate the average salary
print(df[df["salary"] > 70000]) # Filter employees with salary greater than 70000
print(df[df["name"].str.startswith("P")]) # Filter employees whose name starts with 'P'


# Reading data from CSV file
df = pd.read_csv("employees.csv")
print(df)

print("\nEmployee Names:")
print(df["name"])

print("\nTotal Employees:", len(df))
print("\nHighest Salary:", df["salary"].max())
print("\nLowest Salary:", df["salary"].min())
print("\nAverage Salary:", df["salary"].mean())

print(df.info())
print(df.describe())

print(df.head())# Display the first 5 rows of the DataFrame
print(df.tail())# Display the last 5 rows of the DataFrame  
print(df.sample(5))# Display 5 random rows from the DataFrame

print(df[["name", "salary"]])# Access specific columns

print(type(df))# Check the type of the 'name' column
print(df.columns)# Get the column names of the DataFrame
print(df.index)# Get the index of the DataFrame

print(df.columns.tolist())# Convert column names to a list
print(df.describe(include="all"))# Get statistical summary of all columns, including non-numeric ones
print(type(df["name"]))# Check the type of the 'name' column
print(df[:])# Display all rows and columns of the DataFrame
print(df.iloc[0])# Access the first row of the DataFrame using iloc
print(df.loc[0])# Access the first row of the DataFrame using loc

print(df.iloc[0:3])# Access the first three rows of the DataFrame using iloc
