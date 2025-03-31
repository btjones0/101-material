def main():
    val = [10, 20, 30]
    y = func(val)

    print(val, y)


def func(some_other_variable_name):
    some_other_variable_name.append(40)
    return 7


if __name__ == '__main__':
    main()
