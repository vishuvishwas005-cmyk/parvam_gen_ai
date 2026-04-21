# Conditional statements in Python

age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)