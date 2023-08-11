def rotate(matrix):
    '''
    lvl: medium
    :param matrix: дана матрицаНужно перевернуть её по часовой стрелке
    :return: None - нечего не возвращаем, меняем изначальную через синтаксис срезов)
    1, 2, 3,             7, 4, 1,
    4, 5, 6,   --- >>>   8, 5, 2,
    7, 8, 9              9, 6, 3
    '''
    matrix[:] = list(zip(*matrix))
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])[::-1]


# for test
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(rotate(matrix))
# print(*matrix, sep='\n')