from math import sqrt


# Compute the distance between (x1, y1) and (x2, y2)
def distance(x1, y1, x2=0, y2=0):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    print(distance(1, 2, 5, 5))
    print(distance(5, 12))
    # print(distance(5, 12, 0, 0))
    # print(distance(7, 24, 0, 0))
    # print(distance(10, 20, 0, 0))
