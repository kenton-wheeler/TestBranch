import csv

def count_records():
    with open("data/car_prices.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        rows = 0
        for row in csv_reader:
            rows += 1
        print(f"There are {rows} rows in the csv file")

count_records()


