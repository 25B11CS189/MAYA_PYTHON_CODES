s = input().strip().lower()
words = s.split()

vowels = "aeiou"
vowel_counts = [sum(1 for ch in word if ch in vowels) for word in words]

print(min(vowel_counts))s = input().strip().lower()
words = s.split()

vowels = "aeiou"
vowel_counts = [sum(1 for ch in word if ch in vowels) for word in words]

print(min(vowel_counts))
