import unittest

import distance


class Tests(unittest.TestCase):
    def test_distance1(self):
        result = distance.distance(5, 12)
        self.assertAlmostEqual(13, result)


if __name__ == '__main__':
    unittest.main()
