# Simple Python3 program to count digits in a number

n = int(input())

count = 0
while n > 0:
    n //= 10
    count += 1

print(count)
