# Python Lists

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# Accessing elements
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# List operations
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "grape")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# List slicing
print("First 3 numbers:", numbers[:3])
print("Even numbers:", numbers[1::2])

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)