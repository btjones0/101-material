import unittest
from funcs import distance

class Tests(unittest.TestCase):
   def test_distance1(self):
      self.assertEqual(distance(1, 2, 4, 6), 5)

   def test_distance2(self):
      self.assertEqual(distance(-5, 12), 13)


if __name__ == '__main__':
   unittest.main()
