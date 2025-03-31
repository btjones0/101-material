def average(numbers):
    """Returns the mean of the numbers in the given list.

    Args:
        numbers: a list of numbers

    Returns: The arithmetic mean of the numbers in the given list.
    """
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def big_words(words, length):
    """Returns a new list containing all big words from the given list.

    Big here means at least as long as the given length.

    Args:
        words: a list of strings
        length: the minimum length of a "big" word

    Returns: A list of all the "big" words in the given list.
    """
    return [word for word in words if len(word) >= length]
    # big_words = []

    # for word in words:
    #     if len(word) >= length:
    #         big_words.append(word)

    # return big_words
