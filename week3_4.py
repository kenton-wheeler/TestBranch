vowels = ['A','E','I','O','U']
word = input("Please enter a word: ").upper()
number_of_vowels = 0
number_of_consonants = 0
for letter in word:
    if letter in vowels:
        number_of_vowels += 1
    else:
        number_of_consonants += 1
print(f"Number of vowels in the word: {number_of_vowels}")
print(f"Number of consonants in the word: {number_of_consonants}")