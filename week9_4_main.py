from week9_4_process import *
from week9_4_tui import *

data = read_csv_file()
brands = create_brands_list(data)
print(brands)

choice = main_menu()
if choice == 1:
    show_phones_by_brand(data,brands)