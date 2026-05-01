s = input().strip()
words = s.split()
print(" ".join(w[::-1] for w in words[::-1]))
