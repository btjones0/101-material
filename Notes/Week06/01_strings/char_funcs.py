# Write a function called char_upper that returns an uppercase version
# of the input character.  DO NOT CHANGE if not a lowercase character.
def char_upper(char):
    if ord('a') <= ord(char) and ord(char) <= ord('z'):  # is char is lowercase
        return chr(ord(char) - 32)
    else:
        return char


if __name__ == '__main__':
    print(char_upper('a'))  # should print 'A'
    print(char_upper('r'))  # should print 'R'
    print(char_upper('T'))  # should print 'T'
    print(char_upper('?'))  # should print '?'
