import unittest
import funcs

class Tests(unittest.TestCase):
   def test_f1(self):
      self.assertEqual(funcs.f(0), 0)

   def test_f2(self):
      self.assertEqual(funcs.f(-2), 24)

   def test_f3(self):
      self.assertEqual(funcs.f(4), 120)

   def test_g1(self):
      self.assertAlmostEqual(funcs.g(1, 0), 0.33333333)

   def test_g2(self):
      self.assertAlmostEqual(funcs.g(2.3, 4.7), 3.968115942)

   def test_g3(self):
      self.assertAlmostEqual(funcs.g(-3, -1), -1.11111111)

if __name__ == '__main__':
   unittest.main()
