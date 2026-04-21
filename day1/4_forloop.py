# For loops in Python

# Loop through a list
fruits = ["apple", "banana", "cherry", "orange"]

for fruit in fruits:
    print("I like", fruit)

# Loop with range
for i in range(1, 6):
    print("Number:", i)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")