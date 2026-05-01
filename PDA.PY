# Simple Python3 program to classify a number

def sum_of_divisors(n):
    total = 0
    for i in range(1, n // 2 + 1):  # proper divisors are less than n
        if n % i == 0:
            total += i
    return total

N = int(input())

div_sum = sum_of_divisors(N)

if div_sum == N:
    print("PERFECT")
elif div_sum < N:
    print("DEFICIENT")
else:
    print("ABUNDANT")
