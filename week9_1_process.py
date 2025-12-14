import csv

def read_csv_file():
    phones_data = []
    with open("data/mobile_phones.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            phones_data.append(row)
    return phones_data
