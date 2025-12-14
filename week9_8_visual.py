import matplotlib.pyplot as plt

def show_top_10_priced_phones(x,y):
    x.reverse()
    y.reverse()
    plt.title("Top 10 Most Expensive Phones")
    plt.tick_params(axis='y', rotation=45)
    plt.yticks(fontsize=8)
    plt.barh(x,y)
    plt.show()