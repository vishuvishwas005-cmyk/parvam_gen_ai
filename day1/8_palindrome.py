# Check if a string is palindrome

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]

# Test cases
test_strings = ["radar", "A man a plan a canal Panama", "hello", "racecar"]

for string in test_strings:
    result = is_palindrome(string)
    print(f"'{string}' is palindrome: {result}")

# Check palindrome number
def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

numbers = [121, 12321, 123, 1221]
for num in numbers:
    result = is_palindrome_number(num)
    print(f"{num} is palindrome: {result}")