from pet import Pet
# This is new.  We need it for attrgetter seen below.
from operator import attrgetter

pets = []
pets.append(Pet("Oliver", "Iguana", 12))
pets.append(Pet("Charlie", "Mongoose", 7))
pets.append(Pet("Spot", "Dog", 2))
pets.append(Pet("Casper", "Cat", 5))

print("\n-- Unsorted Pets --\n")
for pet in pets:
   print("{:7s} is {:2d} years old.".format(pet.name, pet.age))

# To sort by the attribute name
pets.sort(key=attrgetter('name'))

print("\n-- Sorted by name --\n")
for pet in pets:
   print("{:7s} is {:2d} years old.".format(pet.name, pet.age))

# Another way of sorting.  This uses a cool new thing called a lambda
# function!
pets.sort(key=lambda pet: pet.age)

print("\n-- Sorted by age --\n")
for pet in pets:
   print("{:7s} is {:2d} years old.".format(pet.name, pet.age))
