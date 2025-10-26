height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
for row in range(height):
    for column in range(width):
        print('*',end="")
    print()