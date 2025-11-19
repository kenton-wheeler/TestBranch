def display_menu():
    try:
        print("1. Add a fruit to the list")
        print("2. Remove a fruit from the list")
        print("3. Print the list")
        print("9. Exit")
        menu_option = int(input("Enter a menu option: "))
    except ValueError:
        print("You must enter a number")
        display_menu()
    return menu_option

def option1():
    fruit = input("Enter a fruit to add: ")
    if fruit not in fruits:
        fruits.append(fruit)
    else:
        print(f"{fruit} already in the list")

def option2():
    fruit = input("Enter a fruit to remove: ")
    if fruit in fruits:
        fruits.remove(fruit)
    else:
        print(f"{fruit} is not in the list")

fruits = ['apple', 'banana', 'lemon', 'orange']

while True:
    option_selected = display_menu()
    if option_selected == 1:
        option1()
    elif option_selected == 2:
        option2()
    elif option_selected == 3:
        print(fruits)
    elif option_selected == 9:
        break
    else:
        print("Invalid menu option")