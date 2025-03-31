def insertion_sort(lst):
    for index in range(1, len(lst)):
        insert(lst, index, lst[index])


def insert(lst, location, to_insert):
    while location > 0 and to_insert < lst[location - 1]:
        lst[location] = lst[location - 1]
        location -= 1

    lst[location] = to_insert
