import unittest


class Tests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_addition2(self):
        self.assertAlmostEqual(0.1 + 0.1 + 0.1, 0.3)


if __name__ == '__main__':
    unittest.main()
