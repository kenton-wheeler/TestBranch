import matplotlib.pyplot as plt

phone_sales_2024 = [4550,2056,2805,3490,3792,4333,3845,4243,3600,6634,7850,8122]
phone_sales_2025 = [4601,1556,2300,3204,3998,4655,4062,4752,3825,7230,8330,9606]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

plt.title("Mobile phone sales by months in 2024 and 2025")
plt.xlabel("Month")
plt.ylabel("Phone sales")
plt.plot(months,phone_sales_2024,label="2024")
plt.plot(months,phone_sales_2025,label="2025")
plt.legend(loc="upper left")
plt.show()