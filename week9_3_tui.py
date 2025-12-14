def main_menu():
    print("1.	Show all phones of a given brand")
    print("2.	Display the average price for each brand")
    print("3.	Display a bar chart showing the 10 most expensive phones")
    while True:
        try:
            choice = int(input("Enter menu choice: "))
            if choice not in (1,2,3,4):
                print("Invalid choice, please re-enter")
            else:
                break
        except:
            print("Invalid choice, please re-enter")
    return choice
