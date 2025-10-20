age = int(input("Please enter your age "))
if age <= 16:
    print("You are too young to drive")
else:
    theory_test = input("Have you passed your theory test? (Y/N) ").upper()
    driving_test = input("Have you passed your driving test? (Y/N) ").upper()
    if theory_test == 'N' and driving_test == 'N':
        print("You haven't passed your theory or driving test")
    elif theory_test == 'Y' and driving_test == 'N':
        print("You haven't passed your driving test yet")
    elif theory_test == 'N' and driving_test == 'Y':
        print("You cannot pass your driving test before the theory test")
    else:
        print("You are eligible to drive")
