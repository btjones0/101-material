import unittest
from sorting import selection_sort


class SortTests(unittest.TestCase):
    def test01_empty_sort(self):
        lst = []

        selection_sort(lst)
        self.assertEqual(lst, [])

    def test02_one_element_sort(self):
        lst = [5]

        selection_sort(lst)
        self.assertEqual(lst, [5])

    def test03_two_elements_in_order(self):
        lst = [10, 20]

        selection_sort(lst)
        self.assertEqual(lst, [10, 20])

    def test04_two_elements_reverse_order(self):
        lst = [20, 10]

        selection_sort(lst)
        self.assertEqual(lst, [10, 20])

    def test05_medium_list(self):
        lst = [25, 13, -100, -12, 60, 31, -76, 2]
        selection_sort(lst)
        self.assertEqual(lst, [-100, -76, -12, 2, 13, 25, 31, 60])

    def test06_large_list(self):
        lst = [
            23, 79, 22, 70, 87, 7, 10, 12, 33, 2, 0, 49, 74, 72, 44, 90, 21,
            55, 35, 75, 39, 68, 8, 34, 19, 43, 41, 82, 85, 27, 95, 45, 61, 15,
            63, 76, 36, 83, 66, 48, 5, 77, 62, 53, 11, 94, 80, 67, 88, 20, 65,
            51, 1, 69, 4, 14, 42, 28, 24, 52, 31, 98, 46, 38, 81, 71, 3, 92,
            13, 64, 58, 54, 78, 86, 57, 40, 56, 73, 47, 37, 17, 50, 18, 99, 9,
            60, 84, 59, 25, 29, 96, 32, 97, 26, 91, 16, 30, 93, 6, 89
        ]

        sorted_lst = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
            53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
            87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
        ]

        selection_sort(lst)
        self.assertEqual(lst, sorted_lst)


if __name__ == '__main__':
    unittest.main()
