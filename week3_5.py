for num in range(1,6):
    user_number = int(input(f"Please enter number {num}: "))
    # initialise the lowest and highest numbers to the first number
    # the user enters
    if num == 1:
        lowest = user_number
        highest = user_number
    else:
        if user_number > highest:
            highest = user_number
        if user_number < lowest:
            lowest = user_number
print(f"The lowest number entered is {lowest}")
print(f"The highest number entered is {highest}")