import csv

def read_csv_file():
    phones_data = []
    with open("data/mobile_phones.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            phones_data.append(row)
    return phones_data

def create_brands_list(phones_data):
    brands_list = []
    for row in phones_data:
        if row[0] not in brands_list:
            brands_list.append(row[0])
    return sorted(brands_list)