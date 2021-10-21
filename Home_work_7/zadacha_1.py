class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix

    def __add__(self, other):
        my_list = []

        for item in zip(self.__matrix, other.__matrix):
            my_list.append([j + k for j, k in zip(*item)])

        return Matrix(my_list)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


matrix1 = Matrix([[1, 2, 5], [3, 4, 5], [4, 5, 6]])
print(matrix1, '\n')

matrix2 = Matrix([[10, 20, 2], [30, 40, 2], [100, 2, 1132]])
print(matrix2, '\n')

print(matrix1 + matrix2)
