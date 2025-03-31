# Write a function named sum_2d that takes a list of lists of numbers
# and returns the sum of all the integers in the lists.  First write a
# function sum_row that sums a single list of numbers, then call that
# function from your sum_2d function.
# NOTE: Do *not* use the existing Python sum function.
def sum_2d(list_of_lists):
    total = 0

    # for row_number in range(len(list_of_lists)):
    #     total += sum_row(list_of_lists[row_number])
    for row in list_of_lists:
        total += sum_row(row)

    return total


# row is a list of numbers, sum_row will return the sum of the numbers
# in the row
def sum_row(row):
    total = 0

    for number in row:
        total += number

    return total


if __name__ == '__main__':
    print(sum_2d(
        [[1, 2, 3, 4],
         [10, 13, -4, 7],
         [-3, 102, 17, 0]]))
