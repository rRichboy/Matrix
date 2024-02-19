import random


class Matrix:

    #  Конструктор класса
    def __init__(self, rows=None, columns=None, values=None):
        if values is not None:
            self.Values = values
            self.CountRows = len(values)
            self.CountColumns = len(values[0])
        else:
            if rows is None or columns is None:
                raise ValueError("Specify the number of rows and columns or provide a 2D array")

            self.CountRows = rows
            self.CountColumns = columns
            self.Values = [[random.randint(1, 10) for _ in range(columns)] for _ in range(rows)]

    # Геттер сеттер
    @property
    def CountRows(self):
        return self._count_rows

    @CountRows.setter
    def CountRows(self, value):
        if value <= 0:
            raise ValueError("Number of rows should be greater than 0")
        self._count_rows = value

    @property
    def CountColumns(self):
        return self._count_columns

    @CountColumns.setter
    def CountColumns(self, value):
        if value <= 0:
            raise ValueError("Number of columns should be greater than 0")
        self._count_columns = value

    @property
    def Values(self):
        return self._values

    @Values.setter
    def Values(self, value):
        if not isinstance(value, list) or not all(isinstance(row, list) for row in value):
            raise ValueError("Matrix values should be a 2D list")

        if any(len(row) != len(value[0]) for row in value[1:]):
            raise ValueError("All rows in the matrix should have the same number of columns")

        self._values = value
        self.CountRows = len(value)
        self.CountColumns = len(value[0])

    # Метод для сравнения матриц на равенство
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.Values == other.Values

    # Метод для преобразования матрицы в строку (для удобного вывода)
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.Values])

    # Методы для сложения
    def __add__(self, other):
        if self.CountRows != other.CountRows or self.CountColumns != other.CountColumns:
            raise ArithmeticError("Matrix dimensions do not match for addition")

        result_values = [
            [self.Values[i][j] + other.Values[i][j] for j in range(self.CountColumns)]
            for i in range(self.CountRows)
        ]
        return Matrix(rows=self.CountRows, columns=self.CountColumns, values=result_values)

    # Метод для умножения
    def __mul__(self, other):
        if self.CountColumns != other.CountRows:
            raise ArithmeticError(
                "Number of columns in the first matrix should be equal to the number of rows in the second matrix")

        result_values = [
            [sum(a * b for a, b in zip(row, col)) for col in zip(*other.Values)]
            for row in self.Values
        ]
        return Matrix(rows=self.CountRows, columns=other.CountColumns, values=result_values)

    # Метод для приведения матрицы к верхнетреугольному виду
    def to_upper_triangular(self, matrix):

        rows, cols = len(matrix), len(matrix[0])

        for i in range(min(rows, cols)):
            pivot_row = i
            while pivot_row < rows and matrix[pivot_row][i] == 0:
                pivot_row += 1

            if pivot_row == rows:
                continue

            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

            for j in range(i + 1, rows):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, cols):
                    matrix[j][k] -= factor * matrix[i][k]

        self.Values = matrix


    # Метод для вычисления определителя треугольной матрицы
    def determinant_triangular(self):
        det = 1
        for i in range(self.CountRows):
            det *= self.Values[i][i]
        return det

    # Метод для решения системы линейных уравнений методом обратной подстановки
    def solve_equation_substitution(self):
        if self.CountRows != self.CountColumns - 1:
            raise ValueError("The matrix should be square and augmented with a column of constants.")

        coefficients = [row[:-1] for row in self.Values]
        results = [row[-1] for row in self.Values]

        solutions = [0] * self.CountColumns
        for i in range(self.CountRows - 1, -1, -1):
            total = results[i] - sum(coeff * sol for coeff, sol in zip(coefficients[i][i + 1:], solutions[i + 1:]))
            solutions[i] = total / coefficients[i][i]

        return solutions



