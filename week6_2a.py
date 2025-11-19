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
        for row in csv_reader:
            if row[1] == 'MINI':
                print(f"{row[0]:6} {row[1]:10} {row[2]:20} {row[6]:15}")

count_records()
display_make("MINI")