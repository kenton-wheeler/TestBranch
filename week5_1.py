german_cars = ['Audi','BMW','Mercedes','Porsche','VW']
car_input = input("Enter a make of car (enter End to exit program): ")
while car_input != 'End':
    if car_input in german_cars:
        position = german_cars.index(car_input)
        print (f"{car_input} is in index position {position} in the list")
    else:
        print (f"{car_input} is not in the list")
    car_input = input("Enter a make of car (enter End to exit program): ")