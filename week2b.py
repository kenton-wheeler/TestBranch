age = int(input("Please enter your age "))
if age <= 16:
    print("You are too young to drive")
else:
    theory_test = input("You have passed your theory test? (Y/N) ").upper()
    driving_test = input("You have passed your driving test? (Y/N) ").upper()
    if theory_test == 'Y':
        theory_test = True
    else:
        theory_test = False
    if driving_test == 'Y':
        driving_test = True
    else:
        driving_test = False

    if not theory_test and not driving_test:
        print("You haven't passed your theory or driving test")
    elif theory_test and not driving_test:
        print("You haven't passed your driving test yet")
    elif not theory_test and driving_test:
        print("You cannot pass your driving test before the theory test")
    else:
        print("You are eligible to drive")