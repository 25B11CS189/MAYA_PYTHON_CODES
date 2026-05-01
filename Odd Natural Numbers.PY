# Simple Python3 program to print odd natural numbers <= N

N = int(input())

for i in range(1, N + 1, 2):   # start at 1, step by 2
    print(i, end=" ")
