import csv

def create_animal_dict(file):
    animal_dict = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        key1 = headings[0]
        key2 = headings[1]
        count = 1
        for row in csv_reader:
            key = "animal"+str(count)
            animal_dict[key]={key1:row[0],key2:row[1]}
            count += 1
    return animal_dict

#Main program
marwell_dict = create_animal_dict("data/marwell_zoo.csv")
longleat_dict = create_animal_dict("data/longleat_zoo.csv")
print(marwell_dict)
print(longleat_dict)