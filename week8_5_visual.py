import matplotlib.pyplot as plt
from week8_5_process import *

def draw_pie_chart(makes,sales):
    (makes, sales, avg_prices) = create_lists()
    plt.title("Number of cars sold by make")
    plt.pie(sales,labels=makes,autopct="%.0f%%")
    plt.show()

