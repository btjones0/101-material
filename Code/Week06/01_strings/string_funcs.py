from char_funcs import char_upper


# Write a function called string_upper that returns an uppercase version
# of the input string.
def string_upper(string):
    result = []

    for char in string:
        result.append(char_upper(char))

    return ''.join(result)


if __name__ == '__main__':
    print(string_upper("Hello world!"))  # should print "HELLO WORLD!"
