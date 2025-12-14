from week9_8_process import *
from week9_8_tui import *
from week9_8_visual import *

data = read_csv_file()
brands = create_brands_list(data)
print(brands)

choice = main_menu()
if choice == 1:
    show_phones_by_brand(data,brands)
elif choice == 2:
    brand_avgs = calc_avg_price(data,brands)
    display_brand_avg(brand_avgs)
elif choice == 3:
    x,y = get_top_10_priced_phones(data)
    show_top_10_priced_phones(x,y)
