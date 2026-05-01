# Simple Python3 program for N - S - C

A, B = map(int, input().split())

for n in range(A + 1, B):
    print(n, n**2, n**3)
