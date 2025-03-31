def selection_sort(lst):
    for index in range(len(lst) - 1):
        swap(lst, index, index_of_smallest(lst, index))


def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def index_of_smallest(lst, start):
    min_index = start

    for index in range(start + 1, len(lst)):
        if lst[index] < lst[min_index]:
            min_index = index

    return min_index
