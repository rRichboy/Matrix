import unittest

from Matrix import Matrix


class TestMatrixOperations(unittest.TestCase):

    # Тест инициализации матрицы по заданным размерам
    def test_init_with_dimensions(self):
        matrix = Matrix(rows=3, columns=4)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 4)

    # Тест инициализации матрицы по заданному двумерному массиву
    def test_init_with_2d_array(self):
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(values=values)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест метода преобразования матрицы в строку
    def test_to_string_method(self):
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(values=values)
        expected_output = "1 2 3\n4 5 6\n7 8 9"
        self.assertEqual(str(matrix), expected_output)

    # Тест исключения при сложении матриц с разными размерами
    def test_addition_error_different_dimensions(self):
        matrix1 = Matrix(rows=2, columns=3)
        matrix2 = Matrix(rows=3, columns=2)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 + matrix2

    # Тест корректного результата сложения матриц
    def test_addition_correct_result(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        expected_result = Matrix(values=[[6, 8], [10, 12]])
        result_matrix = matrix1 + matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест исключения при умножении матриц с неподходящими размерами
    def test_multiplication_error_invalid_dimensions(self):
        matrix1 = Matrix(rows=2, columns=3)
        matrix2 = Matrix(rows=4, columns=2)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 * matrix2

    # Тест проверки размеров результата умножения матриц
    def test_multiplication_result_dimensions(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix.CountRows, matrix1.CountRows)
        self.assertEqual(result_matrix.CountColumns, matrix2.CountColumns)

    # Тест корректного результата умножения матриц
    def test_multiplication_correct_result(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        expected_result = Matrix(values=[[19, 22], [43, 50]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест приведения матрицы к верхнетреугольному виду
    def test_upper_triangular_matrix(self):
        matrix = Matrix(values=[[2, 3, 4], [0, 1, 5], [0, 0, 3]])
        matrix.to_upper_triangular()
        expected_matrix = Matrix(values=[[1, 1.5, 2], [0, 1, 5], [0, 0, 1]])
        self.assertEqual(matrix, expected_matrix)

    # Тест вычисления определителя верхнетреугольной матрицы
    def test_determinant_triangular_matrix(self):
        matrix = Matrix(values=[[2, 3, 4], [0, 1, 5], [0, 0, 3]])
        det = matrix.determinant_triangular()
        expected_det = 2 * 1 * 3
        self.assertEqual(det, expected_det)

    # Тест метода решения системы линейных уравнений методом обратной подстановки
    def solve_equation_substitution(self, constants):
        if self.CountColumns - 1 != len(constants):
            raise ValueError("The matrix should be augmented with a column of constants.")

        coefficients = [row[:-1] for row in self.Values]
        results = [row[-1] for row in self.Values]

        solutions = [0] * self.CountColumns
        for i in range(self.CountRows - 1, -1, -1):
            total = results[i] - sum(coeff * sol for coeff, sol in zip(coefficients[i][i + 1:], solutions[i + 1:]))
            solutions[i] = total / coefficients[i][i]

        return solutions


if __name__ == '__main__':
    unittest.main()
