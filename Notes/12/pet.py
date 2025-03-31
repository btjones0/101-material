class Pet:
   """A class to model a pet.

   Attributes:
      name (str): The name of the pet.
      animal (str): The type of animal.
      age (int): The age of the pet.
   """
   def __init__(self, name, animal, age): # Later add age=0
      self.name = name
      self.animal = animal
      self.age = age
