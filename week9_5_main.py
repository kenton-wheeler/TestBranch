from week9_5_process import *
from week9_5_tui import *

data = read_csv_file()
brands = create_brands_list(data)
print(brands)

choice = main_menu()
if choice == 1:
    show_phones_by_brand(data,brands)
elif choice == 2:
    brand_avg = calc_avg_price(data,brands)
    print(brand_avg)