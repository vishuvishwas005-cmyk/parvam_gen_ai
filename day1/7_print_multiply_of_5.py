# Print multiples of 5

# Using for loop
print("Multiples of 5 from 1 to 50:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i, end=" ")
print()

# Using while loop
print("Multiples of 5 using while loop:")
num = 5
while num <= 50:
    print(num, end=" ")
    num += 5
print()

# Print first n multiples of 5
n = 10
print(f"First {n} multiples of 5:")
for i in range(1, n+1):
    print(5 * i, end=" ")
print()