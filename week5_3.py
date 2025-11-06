german_cars=[('Audi',5064),('BMW',6350),('Ford',10954),('Mercedes',4390),('Porsche',755)]

german_cars.append(('VW',8745))
german_cars.remove(('Ford',10954))

for car in german_cars:
    print(f"{car[0]} sold {car[1]} vehicles this year")

japanese_cars = [('Honda',9200),('Lexus',2665),('Mazda',3450),('Suzuki',2885),('Toyota',10330)]
all_cars = sorted(german_cars + japanese_cars)

for car in all_cars:
    print(f"{car[0]} sold {car[1]} vehicles this year")

total_german_cars_sold = 0
total_japanese_cars_sold = 0
for car in german_cars:
    total_german_cars_sold += car[1]
for car in japanese_cars:
    total_japanese_cars_sold += car[1]
if total_german_cars_sold > total_japanese_cars_sold:
    print("More german cars were sold than japanese cars this year")
else:
    print("More japanese cars were sold than german cars this year")