import unittest

import solver_funcs


class TestCases(unittest.TestCase):
    def test_chech_valid_with_finished_puzzle(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))


if __name__ == '__main__':
    unittest.main()
