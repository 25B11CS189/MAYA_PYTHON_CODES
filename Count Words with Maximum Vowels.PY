s = input().strip().lower()
words = s.split()

vowels = "aeiou"
vowel_counts = [sum(1 for ch in word if ch in vowels) for word in words]

max_vowels = max(vowel_counts)
print(vowel_counts.count(max_vowels))
