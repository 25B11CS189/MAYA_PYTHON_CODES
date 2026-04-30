# Simple Python3 program to print multiplication table from A to B

N, A, B = map(int, input().split())

for i in range(A, B + 1):
    print(f"{N} x {i} = {N * i}")
