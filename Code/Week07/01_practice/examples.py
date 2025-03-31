# Returns True if the value is even, False otherwise
def is_even(value):
    return value % 2 == 0

    # if value % 2 == 0:
    #     return True
    # else:
    #     return False


def filter_evens(list_of_values):
    result = []

    for value in list_of_values:
        if is_even(value):
            result.append(value)

    return result


def filter_odds(list_of_values):
    result = []

    for value in list_of_values:
        if not is_even(value):
            result.append(value)

    return result
