# Write a function that computes (and returns) a new list with double the
# entries in the original list.
# >>> double_list([10, 20, 30, 40])
# [20, 40, 60, 80]
def double_list(lst):
    index = 0
    new_list = []

    while index < len(lst):
        new_list.append(lst[index] * 2)
        index += 1

    return new_list


def double_list_for_loop(lst):
    new_list = []

    for index in range(len(lst)):
        new_list.append(lst[index] * 2)

    return new_list


def double_list_for_loop_take_2(lst):
    new_list = []

    for value in lst:
        new_list.append(value * 2)

    return new_list


def double_list_comprehension(lst):
    return [value * 2 for value in lst]


if __name__ == '__main__':
    print(double_list([10, 20, 30, 40]))
    print(double_list_for_loop([10, 20, 30, 40]))
    print(double_list_for_loop_take_2([10, 20, 30, 40]))
    print(double_list_comprehension([10, 20, 30, 40]))
