squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)


words = ["apple", "banana", "orange", "grape", "umbrella", "mango"]
vowel_words = [word for word in words if word[0].lower() in "aeiou"]
print(vowel_words)
