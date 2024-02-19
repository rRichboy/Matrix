import unittest

from Matrix import Matrix


class TestMatrixOperations(unittest.TestCase):

    # Тест 1 инициализации матрицы по заданным размерам
    def test_init_with_dimensions1(self):
        matrix = Matrix(rows=3, columns=4)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 4)

    # Тест 2 инициализации матрицы по заданным размерам
    def test_init_with_dimensions2(self):
        matrix = Matrix(rows=2, columns=4)
        self.assertEqual(matrix.CountRows, 2)
        self.assertEqual(matrix.CountColumns, 4)

    # Тест 3 инициализации матрицы по заданным размерам
    def test_init_with_dimensions3(self):
        matrix = Matrix(rows=3, columns=2)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 2)

    # Тест 4 инициализации матрицы по заданным размерам
    def test_init_with_dimensions4(self):
        matrix = Matrix(rows=5, columns=3)
        self.assertEqual(matrix.CountRows, 5)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест 1 инициализации матрицы по заданному двумерному массиву
    def test_init_with_2d_array1(self):
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(values=values)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест 2 инициализации матрицы по заданному двумерному массиву
    def test_init_with_2d_array2(self):
        values = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        matrix = Matrix(values=values)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест 3 инициализации матрицы по заданному двумерному массиву
    def test_init_with_2d_array3(self):
        values = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        matrix = Matrix(values=values)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест 4 инициализации матрицы по заданному двумерному массиву
    def test_init_with_2d_array4(self):
        values = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
        matrix = Matrix(values=values)
        self.assertEqual(matrix.CountRows, 3)
        self.assertEqual(matrix.CountColumns, 3)

    # Тест 1 метода преобразования матрицы в строку
    def test_to_string_method1(self):
        values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(values=values)
        expected_output = "1 2 3\n4 5 6\n7 8 9"
        self.assertEqual(str(matrix), expected_output)

    # Тест 2 метода преобразования матрицы в строку
    def test_to_string_method2(self):
        values = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        matrix = Matrix(values=values)
        expected_output = "10 20 30\n40 50 60\n70 80 90"
        self.assertEqual(str(matrix), expected_output)

    # Тест 3 метода преобразования матрицы в строку
    def test_to_string_method3(self):
        values = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
        matrix = Matrix(values=values)
        expected_output = "11 22 33\n44 55 66\n77 88 99"
        self.assertEqual(str(matrix), expected_output)

    # Тест 1 исключения при сложении матриц с разными размерами
    def test_addition_error_different_dimensions1(self):
        matrix1 = Matrix(rows=2, columns=3)
        matrix2 = Matrix(rows=3, columns=2)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 + matrix2

    # Тест 2 исключения при сложении матриц с разными размерами
    def test_addition_error_different_dimensions2(self):
        matrix1 = Matrix(rows=4, columns=2)
        matrix2 = Matrix(rows=2, columns=4)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 + matrix2

    # Тест 3 исключения при сложении матриц с разными размерами
    def test_addition_error_different_dimensions3(self):
        matrix1 = Matrix(rows=6, columns=13)
        matrix2 = Matrix(rows=13, columns=6)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 + matrix2

    # Тест 1 корректного результата сложения матриц
    def test_addition_correct_result1(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        expected_result = Matrix(values=[[6, 8], [10, 12]])
        result_matrix = matrix1 + matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест 2 корректного результата сложения матриц
    def test_addition_correct_result2(self):
        matrix1 = Matrix(values=[[11, 22], [33, 44]])
        matrix2 = Matrix(values=[[55, 66], [77, 88]])
        expected_result = Matrix(values=[[66, 88], [110, 132]])
        result_matrix = matrix1 + matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест 1 исключения при умножении матриц с неподходящими размерами
    def test_multiplication_error_invalid_dimensions1(self):
        matrix1 = Matrix(rows=2, columns=3)
        matrix2 = Matrix(rows=4, columns=2)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 * matrix2

    # Тест 2 исключения при умножении матриц с неподходящими размерами
    def test_multiplication_error_invalid_dimensions2(self):
        matrix1 = Matrix(rows=2, columns=3)
        matrix2 = Matrix(rows=4, columns=4)
        with self.assertRaises(ArithmeticError):
            result_matrix = matrix1 * matrix2

    # Тест 1 проверки размеров результата умножения матриц
    def test_multiplication_result_dimensions1(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix.CountRows, matrix1.CountRows)
        self.assertEqual(result_matrix.CountColumns, matrix2.CountColumns)

    # Тест 2 проверки размеров результата умножения матриц
    def test_multiplication_result_dimensions2(self):
        matrix1 = Matrix(values=[[11, 22], [33, 44]])
        matrix2 = Matrix(values=[[55, 66], [77, 88]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix.CountRows, matrix1.CountRows)
        self.assertEqual(result_matrix.CountColumns, matrix2.CountColumns)

    # Тест 1 корректного результата умножения матриц
    def test_multiplication_correct_result1(self):
        matrix1 = Matrix(values=[[1, 2], [3, 4]])
        matrix2 = Matrix(values=[[5, 6], [7, 8]])
        expected_result = Matrix(values=[[19, 22], [43, 50]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест 2 корректного результата умножения матриц
    def test_multiplication_correct_result3(self):
        matrix1 = Matrix(values=[[2, 3], [4, 5]])
        matrix2 = Matrix(values=[[1, 2], [3, 4]])
        expected_result = Matrix(values=[[11, 16], [19, 28]])
        result_matrix = matrix1 * matrix2
        self.assertEqual(result_matrix, expected_result)

    # Тест 1 приведения матрицы к треугольному виду
    def test_upper_triangular_matrix1(self):
        matrix = Matrix(values=[[1, 8, 4], [3, 8, 5], [7, 7, 5]])
        matrix.to_upper_triangular([[1, 8, 4], [3, 8, 5], [7, 7, 5]])
        expected_matrix = Matrix(values=[[1, 8, 4], [0, -16, -7], [0, 0, -1.5625]])
        self.assertEqual(matrix, expected_matrix)

    # Тест 2 приведения матрицы к треугольному виду
    def test_upper_triangular_matrix2(self):
        matrix = Matrix(values=[[2, 3, 9], [1, 9, 3], [2, 4, 6]])
        matrix.to_upper_triangular([[2, 3, 9], [1, 9, 3], [2, 4, 6]])
        expected_matrix = Matrix(values=[[2, 3, 9], [0, 7.5, -1.5], [0, 0, -2.8]])
        self.assertEqual(matrix, expected_matrix)

    # Тест 1 вычисления определителя треугольной матрицы
    def test_determinant_triangular_matrix1(self):
        matrix = Matrix(values=[[2, 3, 4], [0, 1, 5], [0, 0, 3]])
        det = matrix.determinant_triangular()
        expected_det = 2 * 1 * 3
        self.assertEqual(det, expected_det)

    # Тест 2 вычисления определителя треугольной матрицы
    def test_determinant_triangular_matrix2(self):
        matrix = Matrix(values=[[2, 3, 4], [0, 2, 5], [0, 0, 3]])
        det = matrix.determinant_triangular()
        expected_det = 2 * 2 * 3
        self.assertEqual(det, expected_det)

    # Тест 1 метода решения системы линейных уравнений методом обратной подстановки
    def test_solve_equation_substitution1(self):
        matrix = Matrix(values=[[4, 3, 21, 4], [0, 3, 7, 1], [0, 0, 9, 2]])
        if matrix.CountColumns - 1 != matrix.CountRows:
            raise ValueError("The matrix should be augmented with a column of constants.")

        result = matrix.solve_equation_substitution()
        exp_result = [-0.02777777777777768, -0.18518518518518512,  0.2222222222222222, 0]
        self.assertEqual(result, exp_result)

    # Тест 2 метода решения системы линейных уравнений методом обратной подстановки
    def test_solve_equation_substitution2(self):
        matrix = Matrix(values=[[12, 56, 11, 7], [0, 4, 5, 3], [0, 0, 8, 1]])
        if matrix.CountColumns - 1 != matrix.CountRows:
            raise ValueError("The matrix should be augmented with a column of constants.")

        result = matrix.solve_equation_substitution()
        exp_result = [-2.3020833333333335, 0.59375, 0.125, 0]
        self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main()
