import random

def get_guess():
    valid_input = False
    while not valid_input:
        user_input = input("Enter a number between 1 and 100: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input<1 or user_input>100:
                print("Input number between 1 and 100")
            else:
                valid_input = True
        else:
            print("You must enter a number")
    return user_input


rnd = random.randrange(1,100,1)
guess = get_guess()
num_guesses = 1
while guess != rnd:
    if guess < rnd:
        print("Your guess was too low")
    else:
        print("Your guess was too high")
    num_guesses += 1
    guess = get_guess()
print(f"You guessed the number correctly after {num_guesses} attempts")