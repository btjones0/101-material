import unittest

import funcs


class FuncsTests(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(funcs.f(10), 32)

    def test_f2(self):
        self.assertEqual(funcs.f(17), 53)

    def test_is_zero1(self):
        self.assertEqual(funcs.is_zero(0), True)
        # is the same as
        self.assertTrue(funcs.is_zero(0))

    def test_is_zero2(self):
        self.assertFalse(funcs.is_zero(37))

    def test_area_of_rectangle1(self):
        self.assertEqual(funcs.area_of_rectangle(0, 1, 1, 0), 1)

    def test_area_of_rectangle2(self):
        self.assertEqual(funcs.area_of_rectangle(-7, 10, 3, 4), 60)


if __name__ == '__main__':
    unittest.main()
