from math import sqrt


# Let's make a data type for a 2D point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Computes the distance from p1 to p2 where
# p1 and p2 are Points
def distance(p1, p2):
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
