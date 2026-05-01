s = input().strip()
words = s.split()
print(max(len(w) for w in words))
