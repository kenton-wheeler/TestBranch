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

def calc_avg_price(phones_data,brands_list):
    brand_avg = {}
    for brand in brands_list:
        sum = 0
        count = 0
        for row in phones_data:
            if row[0] == brand:
                sum += int(row[5])
                count += 1
        avg = round(sum / count,2)
        brand_avg[brand]=avg
    return brand_avg

def get_top_10_priced_phones(phones_data):
    sorted_by_price = sorted(phones_data, key=lambda x: int(x[5]), reverse=True)
    top_10 = sorted_by_price[:10]
    top_10_phones = []
    top_10_prices = []
    for phone in top_10:
        top_10_phones.append(phone[0]+" "+phone[1])
        top_10_prices.append(int(phone[5]))
    return top_10_phones, top_10_prices