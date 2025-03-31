from pet import Pet


def print_pets(pets):
    for pet in pets:
        print("%s the %s is %d years old." % (
            pet.name, pet.animal, pet.age))


def get_name(pet):
    return pet.name


def get_age(pet):
    return pet.age


def main():
    pets = [
        Pet("Spot", "Dog", 7),
        Pet("Jinx", "Cat", 5),
        Pet("Noodle", "Snake", 4),
        Pet("Chaos", "Snail", 2),
        Pet("George", "Tortoise", 101),
    ]

    print("-- Unsorted Pets --\n")
    print_pets(pets)

    print("\n-- Sorted by name--\n")
    pets.sort(key=get_name, reverse=True)
    print_pets(pets)

    print("\n-- Sorted by age--\n")
    pets.sort(key=get_age)
    print_pets(pets)


if __name__ == '__main__':
    main()
