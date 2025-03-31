def main():
    x = float(input("x: "))
    y = input("y: ")

    z = do_something(x + 3)

    if z < 6.2 and y != "hi":
        y = do_other_thing(y)
    if x > 8:
        x -= 5
    if x > 4:
        x = x ** 2
    else:
        x = x // 3

    print("x: %.1f, y: %s, z: %.2f" % (x, y, z))


def do_something(m):
    n = m / 2
    return n


def do_other_thing(p):
    if len(p) > 4:
        return "long"
    else:
        return "short"


if __name__ == "__main__":
    main()
