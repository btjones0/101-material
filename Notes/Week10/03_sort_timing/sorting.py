# Selection Sort
def selection_sort(lst):
    for index in range(len(lst) - 1):
        small_index = index_of_smallest(lst, index)
        swap(lst, index, small_index)


def index_of_smallest(lst, start):
    min_index = start

    for index in range(start + 1, len(lst)):
        if lst[index] < lst[min_index]:
            min_index = index

    return min_index


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


# Insertion Sort
def insertion_sort(lst):
    for index in range(1, len(lst)):
        insert(lst, index)


def insert(lst, location):
    to_insert = lst[location]

    while location > 0 and to_insert < lst[location - 1]:
        lst[location] = lst[location - 1]
        location -= 1

    lst[location] = to_insert
