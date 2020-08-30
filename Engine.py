class Cell:

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = None
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def set_value(self):
        if len(self.possible_values) == 1:
            self.value = self.possible_values[0]


class Sudoku_Grid:

    def __init__(self, starting_values):
        self.starting_values = starting_values
        self.cells = []
        self.squares = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                      [3, 4, 5, 12, 13, 14, 21, 22, 23],
                      [6, 7, 8, 15, 16, 17, 24, 25, 26],
                      [27, 28, 29, 36, 37, 38, 45, 46, 47],
                      [30, 31, 32, 39, 40, 41, 48, 49, 50],
                      [33, 34, 35, 42, 43, 44, 51, 52, 53],
                      [54, 55, 56, 63, 64, 65, 72, 73, 74],
                      [57, 58, 59, 66, 67, 68, 75, 76, 77],
                      [60, 61, 62, 69, 70, 71, 78, 79, 80]
                      ]

    def create_grid(self):
        for y in range(9):
            for x in range(9):
                self.cells.append(Cell(x, y))
        for i in range(81):
            if self.starting_values[i] != 0:
                self.cells[i].value = self.starting_values[i]

    def update_cell_values(self):
        self.update_columns_x()
        self.update_rows_y()
        self.update_squares()
        for i in range(81):
            self.cells[i].set_value()

    def update_columns_x(self):
        for i in range(9):
            column = []
            for j in range(9):
                if self.cells[i + (9 * j)].value is not None:
                    column.append(self.cells[i + (9 * j)].value)
            for k in range(9):
                for digit in column:
                    for value in self.cells[i + (9 * k)].possible_values:
                        if value == digit:
                            self.cells[i + (9 * k)].possible_values.remove(value)

    def update_rows_y(self):
        for i in range(9):
            row = []
            for j in range(9):
                if self.cells[j + (9 * i)].value is not None:
                    row.append(self.cells[j + (9 * i)].value)
            for k in range(9):
                for digit in row:
                    for value in self.cells[k + (9 * i)].possible_values:
                        if value == digit:
                            self.cells[k + (9 * i)].possible_values.remove(value)


    def update_squares(self):
        for i in range(9):
            square = []
            for index in self.squares[i]:
                if self.cells[index].value is not None:
                    square.append(self.cells[index].value)
            for index in self.squares[i]:
                for digit in square:
                    for value in self.cells[index].possible_values:
                        if value == digit:
                            self.cells[index].possible_values.remove(value)
                            print("value {} is not possible".format(value))

    def print_grid(self):
        for i in range(9):
            row = ""
            for j in range(9):
                if self.cells[j + (9 * i)].value is not None:
                    row += str(self.cells[j + (9 * i)].value)
                else:
                    row += "?"
            print(row)

    def solve(self):
        self.create_grid()
        while True:
            self.update_cell_values()
            finished = False
            for i in range(81):
                if self.cells[i].value is None:
                    break
                if i == 80:
                    finished = True
            if finished == True:
                break
            self.print_grid()
            print(" ")
        return self.cells
