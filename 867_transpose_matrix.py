def transpose(matrix):
    '''
    :param matrix: двумерный список на вход
    :return: классическая перевернутая матрица на выход. Строки должны стать столбцами
    Как и всегда решить можно несколькими способами. Можно через зип, но мы решим по классике
    с помощью циклов. Сначала создадим болванку, а далее заменим значения из стартовой матрицы
    '''
    newMatrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[j][i] = matrix[i][j]
    return newMatrix

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(transpose(matrix))