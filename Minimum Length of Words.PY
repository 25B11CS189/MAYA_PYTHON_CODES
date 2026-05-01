s = input().strip()
words = s.split()
print(min(len(w) for w in words))
