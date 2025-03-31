# Write a function called contains that takes in a list of numbers and a
# value for which to search.  The function will return True if the list
# contains the value and False otherwise.
def contains(list_of_numbers, value):
    for number in list_of_numbers:
        if number == value:
            return True

    return False


# Write a function called index_of that takes in a list of numbers and a
# value for which to search.  The function will return the index of the
# first item equal to the given value or -1 if no such item exists.
def index_of(list_of_numbers, value):
    for index in range(len(list_of_numbers)):
        if list_of_numbers[index] == value:
            return index

    return -1


if __name__ == '__main__':
    print(contains([10, 20, 30, 40], 10))  # should be True
    print(contains([10, 20, 30, 40], 20))  # should be True
    print(contains([10, 20, 30, 40], 50))  # should be False

    print(index_of([10, 20, 30, 40], 10))  # should be 0
    print(index_of([10, 20, 30, 40], 20))  # should be 1
    print(index_of([10, 20, 30, 40], 50))  # should be -1
