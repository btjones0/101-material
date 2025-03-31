def main():
    x = 1
    y = 2
    z = func(x + y)

    print("x = %d, y = %d, z = %d" % (x, y, z))


def func(x):
    y = 7
    x += 1
    return x + y


if __name__ == '__main__':
    main()
