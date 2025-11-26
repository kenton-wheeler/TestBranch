import csv

def create_animal_set(file):
    animal_set = set()
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        for row in csv_reader:
            animal_set.add(row[0])
    return animal_set

#Main program
marwell_set = create_animal_set("data/marwell_zoo.csv")
longleat_set = create_animal_set("data/longleat_zoo.csv")
print(f"The animals in Marwell Zoo are {marwell_set}")
print(f"The animals in Longleat Zoo are {longleat_set}")