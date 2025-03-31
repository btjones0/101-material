def main():
    x = int(input("x: "))
    y = int(input("y: "))

    print_stuff(x, y)


def print_stuff(x, y):
    print("A")
    if x > 10:
        if y == 5:
            print("B")
        else:
            print("C")
        print("D")
    elif x > 30 or y < 3:
        print("E")

    print("F")

    if y >= 5:
        print("G")


if __name__ == '__main__':
    main()
