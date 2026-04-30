# Read input character
ch = input().strip()

# Check if character is a vowel
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("VOWEL")
else:
    print("CONSONANT")
