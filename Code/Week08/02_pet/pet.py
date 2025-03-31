class Pet:
    """A class to model a pet."""
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age

    def __repr__(self):
        return 'Pet(%r, %r, %r)' % (self.name, self.animal, self.age)
