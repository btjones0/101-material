def shape1(size):
    i = 0
    j = 0

    while i < size:
        while j < size:
            if i == j or i + j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')

            j += 1

        print()
        i += 1
        j = 0


if __name__ == '__main__':
    shape1(5)
