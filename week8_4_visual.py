import matplotlib.pyplot as plt
from week8_4_process import *

def draw_bar_chart():
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