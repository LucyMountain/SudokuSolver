import unittest
from Engine import Sudoku_Grid

class MyTestCase(unittest.TestCase):
    def checkGridsEqual(self, grid1, grid2):
        self.assertEqual("Check same number of rows", len(grid1), len(grid2))
        for i in range(len(grid1)):
            self.assertEqual("Check same number of elements in the row", len(grid1[i]), len(grid2[i]))
            for j in range(len(grid1[i])):
                self.assertEqual("Check element ({i}, {j})".format(i=i, j=j),  grid1[i][j], grid2[i][j])

    def testSudokuSolver(self):
        tests = [
            {
                'input': [
                    0, 0, 3, 0, 0, 7, 0, 1, 0,
                    8, 0, 5, 9, 0, 0, 4, 7, 0,
                    0, 0, 0, 6, 0, 5, 0, 9, 0,
                    0, 4, 1, 0, 0, 0, 6, 0, 0,
                    3, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 7, 6, 0, 0, 0, 2, 0, 0,
                    0, 0, 0, 5, 0, 8, 0, 2, 0,
                    2, 0, 9, 7, 0, 0, 3, 8, 0,
                    0, 0, 7, 0, 0, 2, 0, 6, 0,
                ],
                'output' : [
                    4, 9, 3, 8, 2, 7, 5, 1, 6,
                    8, 6, 5, 9, 1, 3, 4, 7, 2,
                    7, 1, 2, 6, 4, 5, 8, 9, 3,
                    5, 4, 1, 2, 7, 9, 6, 3, 8,
                    3, 2, 8, 1, 5, 6, 7, 4, 9,
                    9, 7, 6, 3, 8, 4, 2, 5, 1,
                    6, 3, 4, 5, 9, 8, 1, 2, 7,
                    2, 5, 9, 7, 6, 1, 3, 8, 4,
                    1, 8, 7, 4, 3, 2, 9, 6, 5,
                ]
            }
        ]

        for testCase in tests:
            grid = Sudoku_Grid(testCase['input'])
            solution = grid.solve()
            self.checkGridsEqual(testCase['output'], solution)




if __name__ == '__main__':
    unittest.main()
