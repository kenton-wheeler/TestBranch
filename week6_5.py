import csv

def count_records():
    with open("data/car_prices.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        rows = 0
        for row in csv_reader:
            rows += 1
        print(f"There are {rows} rows in the csv file")

def display_make(make):
    with open("data/car_prices.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        print(f"{headings[0]:6} {headings[1]:10} {headings[2]:20} {headings[6]:15}")
        print()
        matches = False
        for row in csv_reader:
            if row[1] == make:
                print(f"{row[0]:6} {row[1]:10} {row[2]:20} {row[6]:15}")
                matches = True
        if matches == False:
            print("No data found")

def calc_avg_selling_price(make):
    selling_prices = []
    with open("data/car_prices.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            if row[1] == make:
                selling_prices.append(int(row[6]))
        avg_selling_price=round(sum(selling_prices)/len(selling_prices),2)
        return avg_selling_price

def list_all_makes():
    all_makes = []
    with open("data/car_prices.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            if row[1] not in all_makes:
                all_makes.append(row[1])
    return all_makes

def write_sales_summary(makes_list):
    csv_file = open("data/car_sales_summary.csv", "w")
    csv_file.write("make,avg_selling_price\n")
    for make in makes_list:
        avg = calc_avg_selling_price(make)
        csv_data = make+","+str(avg)+"\n"
        csv_file.write(csv_data)
    csv_file.close()
    print("car_sales_summary.csv file created")


count_records()
user_make = input("Enter a make of car: ")
display_make(user_make)
avg = calc_avg_selling_price(user_make)
print(f"The average selling price of {user_make} vehicles is £{avg}")
all_makes = list_all_makes()
write_sales_summary(all_makes)
