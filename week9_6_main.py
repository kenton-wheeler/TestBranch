from week9_6_process import *
from week9_6_tui import *

data = read_csv_file()
brands = create_brands_list(data)
print(brands)

choice = main_menu()
if choice == 1:
    show_phones_by_brand(data,brands)
elif choice == 2:
    brand_avgs = calc_avg_price(data,brands)
    display_brand_avg(brand_avgs)