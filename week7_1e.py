set1 = {2,5,7,11,15,4}
set2 = {4,6,2,9,11,14}

print(f"Set1 is {set1}")
print(f"Set2 is {set2}")

set1.add(8)
set2.add(4)

print()
print(f"Set1 is {set1}")
print(f"Set2 is {set2}")

set1.discard(11)
set2.discard(5)
print()
print(f"Set1 is {set1}")
print(f"Set2 is {set2}")

set_union = set1.union(set2)
print()
print(f"The union of set1 and set2 is {set_union}")

set_common = set1.intersection(set2)
print()
print(f"The numbers common to set1 and set2 are {set_common}")