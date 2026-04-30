# Simple Python3 program to find sum of all digits

n = int(input())

total = 0
while n > 0:
    total += n % 10   # add last digit
    n //= 10          # remove last digit

print(total)
