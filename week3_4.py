word = input("Please enter a word: ").upper()
number_of_vowels = 0
number_of_consonants = 0
for position in range(len(word)):
    letter = word[position]
    if letter in ('A','E','I','O','U'):
        number_of_vowels += 1
    else:
        number_of_consonants += 1
print(f"Number of vowels in the word: {number_of_vowels}")
print(f"Number of consonants in the word: {number_of_consonants}")