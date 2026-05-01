s = input().strip()
vowels = "aeiou"
missing = [v for v in vowels if v not in s]

if missing:
    print(" ".join(missing))
else:
    print(0)
