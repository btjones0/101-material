# Write a function rev_string that takes a string as input.  The
# function will return a new string such that the characters are in
# reversed order.
def rev_string(string):
    result = []

    for index in range(len(string) - 1, -1, -1):
        result.append(string[index])

    return ''.join(result)


if __name__ == '__main__':
    print(rev_string("Hello world!"))  # should print "!dlrow olleH"
