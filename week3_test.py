user_word = input("Please enter a word: ").upper()
for position in range(len(user_word)-1, -1, -1):
    print(user_word[position])
