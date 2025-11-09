def summarise_numbers(numbers_list):
    total = sum(numbers_list)
    count = len(numbers_list)
    avg = total/count
    return (total,count,avg)

# Main program
user_number = int(input("Enter the next number (0 to exit) "))
numbers_list = []
while user_number != 0:
    numbers_list.append(user_number)
    user_number = int(input("Enter the next number (0 to exit) "))

summary = summarise_numbers(numbers_list)
print(f"The total of the numbers is {summary[0]}")
print(f"The count of the numbers is {summary[1]}")
print(f"The average of the numbers is {summary[2]}")

# (sum,count,avg) = summarise_numbers(numbers_list)
# print(f"The total of the numbers is {sum}")
# print(f"The count of the numbers is {count}")
# print(f"The average of the numbers is {avg}")