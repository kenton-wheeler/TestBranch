size = int(input("Enter the size of the triangle: "))
for row in range(1,size+1):
    for column in range(row):
        print('#',end="")
    print()