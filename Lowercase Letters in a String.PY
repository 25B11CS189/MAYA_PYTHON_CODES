s = input().strip()
count = sum(1 for ch in s if ch.islower())
print(count)
