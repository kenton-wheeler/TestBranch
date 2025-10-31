# Function to calculate the total of three numbers
def calc_total(number1, number2, number3):
    total = number1 + number2 + number3
    return total

# Function to calculate the average of three numbers
def calc_avg(number1, number2, number3):
    avg = (number1 + number2 + number3)/3
    return avg

# Function to sort three numbers into numerical order
def sort_numbers(number1, number2, number3):
    num_list = [number1,number2,number3]
    print(f"Sorted in numerical order, the numbers are {sorted(num_list)}")


# Main program
# Prompt user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the calc_total function
total = calc_total(num1, num2, num3)

# Display the total
print(f"The total is: {total}")

# Call the calc_avg function
average = calc_avg(num1, num2, num3)

# Display the average
print(f"The average is: {average:.2f}")

# Call the sort_numbers function to display the numbers in numerical order lowest first
sort_numbers(num1, num2, num3)