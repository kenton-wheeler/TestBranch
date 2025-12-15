def main_menu():
    print("1.	Show all phones of a given brand")
    print("2.	Display the average price for each brand")
    print("3.	Display a bar chart showing the 10 most expensive phones")
    while True:
        try:
            choice = int(input("Enter menu choice: "))
            if choice not in (1,2,3):
                print("Invalid choice, please re-enter")
            else:
                break
        except:
            print("Invalid choice, please re-enter")
    return choice

def show_phones_by_brand(phones_data, brands_list):
    while True:
        user_brand = input("Enter a phone brand: ")
        if user_brand in brands_list:
            print(f"Model                Storage    RAM    Price")
            for row in phones_data:
                if row[0] == user_brand:
                   print(f"{row[1]:20} {row[2]:10} {row[3]:10} {row[5]:10}")
            break
        else:
            print("Invalid brand, please re-enter")