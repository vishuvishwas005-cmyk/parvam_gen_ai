# Count number of digits in a number

def count_digits(number):
    if number == 0:
        return 1
    count = 0
    number = abs(number)  # Handle negative numbers
    while number > 0:
        count += 1
        number = number // 10
    return count

# Test the function
test_numbers = [0, 123, 456789, -12345, 1000000]

for num in test_numbers:
    digits = count_digits(num)
    print(f"Number of digits in {num}: {digits}")

# Alternative using logarithm
import math

def count_digits_log(number):
    if number == 0:
        return 1
    return int(math.log10(abs(number))) + 1

print("Using logarithm method:")
for num in test_numbers:
    digits = count_digits_log(num)
    print(f"Number of digits in {num}: {digits}")