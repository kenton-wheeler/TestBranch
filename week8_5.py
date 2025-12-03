import csv
import matplotlib.pyplot as plt

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

(makes,sales,avg_prices) = create_lists()
print(makes)
print(sales)
print(avg_prices)

plt.title("Number of cars sold by make")
plt.pie(sales,labels=makes,autopct="%.0f%%")
plt.show()