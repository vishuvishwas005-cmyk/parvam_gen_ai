# Python Sets

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates a dict, not set

print("Fruits set:", fruits)
print("Numbers set:", numbers)
print("Empty set:", empty_set)

# Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Adding multiple elements
fruits.update(["grape", "pineapple"])
print("After update:", fruits)

# Removing elements
fruits.remove("banana")  # Raises KeyError if not found
print("After remove:", fruits)

fruits.discard("kiwi")  # Doesn't raise error if not found
print("After discard:", fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)
print("Set2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print("Squares set:", squares)

even_set = {x for x in range(1, 11) if x % 2 == 0}
print("Even numbers set:", even_set)

# Checking membership
print("Is 3 in set1?", 3 in set1)
print("Is 7 in set1?", 7 in set1)