class Pet:
    """A class to model a pet.

    Attributes:
        name: The name of the pet.
        animal: The type of animal.
        age: The age of the pet.
    """
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age

    def __repr__(self):
        return 'Pet(%r, %r, %r)' % (self.name, self.animal, self.age)

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.animal == other.animal and
            self.age == other.age
        )
