import csv

def create_lists():
    makes_list = []
    num_sold_list = []
    avg_price_list = []
    with open("data/car_sales.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            makes_list.append(row[0])
            num_sold_list.append(int(row[1]))
            avg_price_list.append(int(row[2]))
    return (makes_list,num_sold_list,avg_price_list)