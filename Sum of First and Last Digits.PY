# Simple Python3 program to find sum of first and last digit

n = int(input())

# Last digit
last_digit = n % 10

# First digit
first_digit = n
while first_digit >= 10:
    first_digit //= 10

# Sum
print(first_digit + last_digit)
