s = input().strip()
vowels_lower = set("aeiou")
vowels_upper = set("AEIOU")

if vowels_lower.issubset(set(s)) or vowels_upper.issubset(set(s)):
    print("True")
else:
    print("False")
