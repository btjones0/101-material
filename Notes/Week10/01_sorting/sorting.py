def selection_sort(lst):
    for starting_index in range(len(lst) - 1):
        small_index = index_of_smallest(lst, starting_index)
        swap(lst, starting_index, small_index)


def index_of_smallest(lst, starting_index):
    small_index = starting_index

    for index in range(starting_index + 1, len(lst)):
        if lst[index] < lst[small_index]:
            small_index = index

    return small_index


def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
