# While loops in Python

# Basic while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# While loop with break
number = 1
while number <= 10:
    print("Number:", number)
    if number == 5:
        break
    number += 1

# While loop with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print("Odd number:", num)