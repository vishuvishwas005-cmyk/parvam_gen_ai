# Check if a number is prime

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
test_numbers = [2, 3, 4, 5, 17, 18, 23, 29, 97, 100]

for num in test_numbers:
    result = is_prime(num)
    print(f"{num} is prime: {result}")

# Print all prime numbers up to n
def primes_up_to_n(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

n = 50
prime_list = primes_up_to_n(n)
print(f"Prime numbers up to {n}: {prime_list}")