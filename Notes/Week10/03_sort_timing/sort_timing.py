import random
import sys
import time

from sorting import selection_sort


def time_sort(size):
    my_list = random.choices(range(1000000), k=size)

    start_time = time.time()
    # selection_sort(my_list)
    my_list.sort()
    end_time = time.time()

    return end_time - start_time


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
    duration = time_sort(size)

    print('Selection sort (%d elements): %.3f seconds' % (size, duration))


if __name__ == '__main__':
    main()
