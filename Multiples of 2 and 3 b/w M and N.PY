# Simple Python3 program to count numbers divisible by both 2 and 3 between M and N

M, N = map(int, input().split())

count = 0
for i in range(M, N + 1):
    if i % 6 == 0:   # divisible by both 2 and 3
        count += 1

print(count)
