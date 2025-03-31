import sys


def do_some_code(size):
    total = 0

    for val in range(size):
        for val2 in range(size):
            total += val * val2

    return total


def get_size(argv):
    if len(argv) < 2:
        print('ERROR: Missing size')
        sys.exit(1)
    elif len(argv) > 2:
        print('ERROR: Too many arguments')
        sys.exit(1)

    try:
        return int(argv[1])
    except ValueError:
        print('ERROR: Invalid size %r' % argv[1])
        sys.exit(1)


def main():
    size = get_size(sys.argv)
    do_some_code(size)


if __name__ == '__main__':
    main()
