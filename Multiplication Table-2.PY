# Simple Python3 program to print multiplication table up to R terms

N, R = map(int, input().split())

for i in range(1, R + 1):
    print(f"{N} x {i} = {N * i}")
