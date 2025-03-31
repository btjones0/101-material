import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y)
        )
        # return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)
