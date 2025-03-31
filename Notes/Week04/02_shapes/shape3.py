def shape3(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == '__main__':
    shape3(5)
