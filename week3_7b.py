size = int(input("Enter the size of the triangle: "))
for row in range(1,size+1):
    for column in range(row):
        # if the current row is an odd number (not divisible by 2),
        # print a line of < otherwise print a line of >
        if row % 2 != 0:
            print('<',end="")
        else:
            print('>',end="")
    print()