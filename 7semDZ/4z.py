"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string_matrix = ''
        for i in self.matrix:
            for j in i:
                string_matrix += f'{j} '
            string_matrix += '\n'
        return string_matrix

    def __add__(self, other):
        last_matrix = []
        for i in range(len(self.matrix)):
            temp_matrix = []
            for j in range(len(self.matrix)):
                temp_matrix.append(self.matrix[i][j] + other.matrix[i][j])
            last_matrix.append(temp_matrix)
        return Matrix(last_matrix)


matrix_1 = Matrix([[5, 8, 4], [2, 5, 3], [6, 2, 8]])
matrix_2 = Matrix([[7, 6, 2], [4, 2, 5], [4, 5, 2]])
matrix_3= matrix_1 + matrix_2
print(f'1 матрица:\n{matrix_1}')
print(f'2 матрица:\n{matrix_2}')
print(f'3 матрица = 1 матрица + 2 матрица:\n{matrix_3}')