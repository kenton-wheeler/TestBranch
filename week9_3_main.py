from week9_3_process import *
from week9_3_tui import *

data = read_csv_file()
brands = create_brands_list(data)
print(brands)

choice = main_menu()