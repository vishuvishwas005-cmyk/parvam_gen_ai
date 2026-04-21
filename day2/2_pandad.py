# Introduction to Pandas

import pandas as pd
import numpy as np

# Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Creating Series
ages = pd.Series([25, 30, 35, 40], name='Age')
print("Series:")
print(ages)
print()

# Reading from CSV (if file exists)
# df_csv = pd.read_csv('data.csv')

# DataFrame operations
print("First 2 rows:")
print(df.head(2))
print()

print("Last 2 rows:")
print(df.tail(2))
print()

print("DataFrame info:")
print(df.info())
print()

print("Descriptive statistics:")
print(df.describe())
print()

# Selecting columns
print("Names column:")
print(df['Name'])
print()

# Selecting rows
print("Row with index 1:")
print(df.loc[1])
print()

# Filtering
print("People older than 30:")
print(df[df['Age'] > 30])
print()

# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print("DataFrame with Salary:")
print(df)
print()

# Grouping
grouped = df.groupby('City').mean()
print("Grouped by City (mean):")
print(grouped)