# Count and sum of digits in a given number

def count_and_sum_digits(number):
    number = abs(number)  # Handle negative numbers
    count = 0
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        count += 1
        number = number // 10
    return count, total

# Test the function
test_numbers = [123, 456789, 0, 100, 999999]

for num in test_numbers:
    digit_count, digit_sum = count_and_sum_digits(num)
    print(f"Number: {num}")
    print(f"  Digit count: {digit_count}")
    print(f"  Digit sum: {digit_sum}")
    print()

# Alternative using string method
def count_and_sum_digits_str(number):
    num_str = str(abs(number))
    count = len(num_str)
    total = sum(int(digit) for digit in num_str)
    return count, total

print("Using string method:")
for num in test_numbers:
    digit_count, digit_sum = count_and_sum_digits_str(num)
    print(f"Number: {num} -> Count: {digit_count}, Sum: {digit_sum}")