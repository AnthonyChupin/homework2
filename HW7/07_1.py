""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования
матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д."""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
#        for i in self.matrix:
 #           list1 = []
  #          list1.extend(i)
   #         print('     '.join([str(i) for i in list1]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in self.matrix]))

    def __add__(self, other):
        summ = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summ[i][j] = self.matrix[i][j]+other.matrix[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in summ]))


list = [[10, 1, 11],
        [22, 22, 2],
        [3, 33, 3]]
list2 = [[1, 10, 0],
        [200, 200, 220],
        [30, 0, 30]]
matrix1 = Matrix(list)
matrix2 = Matrix(list2)
print(matrix1)
print('---------------')
print(matrix2)
print('---------------')
print(matrix1 + matrix2)