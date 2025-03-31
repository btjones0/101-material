import unittest

from point import Point
from point_funcs import move_up_one


class Tests(unittest.TestCase):
    def test_move_up_one(self):
        self.assertEqual(
            move_up_one(Point(3, 4)),
            Point(3, 5)
        )


if __name__ == '__main__':
    unittest.main()
