# f(x) = 3x + 2
def f(x):
    return 3 * x + 2


# return True if the value is zero, False otherwise
def is_zero(value):
    return value == 0


def area_of_rectangle(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    return width * height


def returns_five():
    return 5


def prints_hello_world():
    print("Hello world")
