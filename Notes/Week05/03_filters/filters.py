# Write a function that computes (and returns) a new list with only the even
# values from the original list.
# >>> filter_evens([14, 3, 97, 65, 102, 17, 0, 4])
# [14, 102, 0, 4]
def filter_evens(lst):
    index = 0
    new_list = []

    while index < len(lst):
        if lst[index] % 2 == 0:
            new_list.append(lst[index])

        index += 1

    return new_list


def filter_evens_for_loop(lst):
    new_list = []

    for value in lst:
        if value % 2 == 0:
            new_list.append(value)

    return new_list


def filter_evens_list_comprehension(lst):
    return [value for value in lst if value % 2 == 0]


if __name__ == '__main__':
    print(filter_evens([14, 3, 97, 65, 102, 17, 0, 4]))
    print(filter_evens_for_loop([14, 3, 97, 65, 102, 17, 0, 4]))
    print(filter_evens_list_comprehension([14, 3, 97, 65, 102, 17, 0, 4]))
