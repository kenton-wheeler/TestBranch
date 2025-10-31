# Function to calculate the total of three numbers
def calc_total(number1, number2, number3):
    total = number1 + number2 + number3
    return total

# Main program
# Prompt user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the calc_total function
total = calc_total(num1, num2, num3)

# Display the total
print(f"The total is: {total}")