# Simple Python3 program to find LCM of two numbers

import math

M, N = map(int, input().split())

lcm = (M * N) // math.gcd(M, N)

print(lcm)
