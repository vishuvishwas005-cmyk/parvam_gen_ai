# Python Tuples

# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_element = (42,)  # Note the comma
empty_tuple = ()

print("Coordinates:", coordinates)
print("Colors:", colors)
print("Single element:", single_element)
print("Empty tuple:", empty_tuple)

# Accessing elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuple unpacking
x, y = coordinates
print(f"x = {x}, y = {y}")

# Tuples are immutable
# colors[0] = "yellow"  # This would raise an error

# Tuple methods
print("Count of 'red':", colors.count("red"))
print("Index of 'green':", colors.index("green"))

# Converting between list and tuple
color_list = list(colors)
color_list.append("yellow")
colors = tuple(color_list)
print("Updated colors:", colors)

# Tuple as dictionary key (since immutable)
locations = {
    (10, 20): "Home",
    (15, 25): "Office",
    (5, 10): "Park"
}
print("Location at (10, 20):", locations[(10, 20)])