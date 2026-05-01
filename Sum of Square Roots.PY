# Simple Python3 program to find sum of square roots from A to B

import math

A, B = map(int, input().split())

total = 0
for i in range(A, B + 1):
    if i >= 0:   # square root is defined only for non-negative numbers
        total += math.sqrt(i)

print(f"{total:.2f}")
