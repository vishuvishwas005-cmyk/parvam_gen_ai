# Python Dictionaries

# Creating dictionaries
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

empty_dict = {}
another_dict = dict(name="Jane", age=25)

print("Person dict:", person)
print("Empty dict:", empty_dict)
print("Another dict:", another_dict)

# Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Country:", person.get("country", "Not specified"))  # Default value

# Adding/modifying values
person["email"] = "john@example.com"
person["age"] = 31
print("Updated person:", person)

# Removing values
removed_age = person.pop("age")
print("Removed age:", removed_age)
print("Person after pop:", person)

# Dictionary methods
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Iterating over dictionary
print("Iterating over keys:")
for key in person:
    print(f"{key}: {person[key]}")

print("Iterating over items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares dict:", squares_dict)

# Nested dictionaries
company = {
    "employees": {
        "john": {"age": 30, "role": "developer"},
        "jane": {"age": 25, "role": "designer"}
    },
    "departments": ["engineering", "design", "marketing"]
}

print("John's role:", company["employees"]["john"]["role"])