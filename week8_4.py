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

plt.title("Average selling prices by car make")
plt.xlabel("Make of car")
plt.ylabel("Average Selling Price")
plt.tick_params(axis='x', rotation=45)
plt.bar(makes,avg_prices)
plt.show()

