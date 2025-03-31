class Pet:
   def __init__(self, name, animal, age):
      self.name = name
      self.animal = animal
      self.age = age

   def __eq__(self, other):
      return (self.name == other.name and
              self.animal == other.animal and
              self.age == other.age)

   # Ask for a printing format.  Then make the __str__ method print
   # that format.  Print now prints a pretty format!
   def __str__(self):
      return ("Name: {:8s} Animal: {:9s} Age: {:2d}"
              .format(self.name, self.animal, self.age))

   # And while that's great and all, it's hard for Python to parse...
   # By which I mean, if someone gave you pet data like that, it
   # would be a pain.  It's such a poor representation of a Pet.
   # Let's make a better representation!
   def __repr__(self):
      return ("Pet('{:s}', '{:s}', {:d})"
              .format(self.name, self.animal, self.age))


if __name__ == '__main__':
   pets = []
   pets.append(Pet("Oliver", "Iguana", 12))
   pets.append(Pet("Charlie", "Mongoose", 7))
   pets.append(Pet("Spot", "Dog", 2))
   pets.append(Pet("Casper", "Cat", 5))

   for pet in pets:
      print(pet)
