import unittest

import funcs


class Tests(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(funcs.f(0), 3)

    def test_f2(self):
        self.assertEqual(funcs.f(4), 5)


if __name__ == '__main__':
    unittest.main()
