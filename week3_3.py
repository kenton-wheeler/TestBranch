user_number = int(input("Enter a number greater than 1: "))
sum = 0
for num in range(1,user_number+1):
    sum += num
print(f"The sum of the numbers from 1 to {user_number} is {sum}")