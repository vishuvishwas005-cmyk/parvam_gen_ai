# Sum of digits of a number

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total

# Test the function
num = 12345
result = sum_of_digits(num)
print(f"Sum of digits of {num} is {result}")

# Alternative using string conversion
def sum_of_digits_str(number):
    return sum(int(digit) for digit in str(number))

result2 = sum_of_digits_str(num)
print(f"Sum using string method: {result2}")