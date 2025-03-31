def shape1(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == '__main__':
    shape1(5)
