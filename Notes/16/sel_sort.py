def selection_sort(lst):
    for index in range(len(lst) - 1):
        small_index = index_of_smallest(lst, index)

        swap(lst, index, small_index)


# Remind them again that functions can modify lists!
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
