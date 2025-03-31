def shape2(size):
    i = 0
    j = 0

    while i < size:
        while j < size:
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')

            j += 1

        print()
        i += 1
        j = 0


if __name__ == '__main__':
    shape2(5)
