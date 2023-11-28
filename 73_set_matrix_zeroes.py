def setZeroes(matrix: list) -> None:
    '''
    :param matrix: дана матрица заполненная нулями и единицами
    :return: ничего не возвращаем. Нужно изменить матрицу. Логика такая: если в строке есть ноль, то вся строка
    должна быть заполнена нулями. Если в столбце есть ноль, то весь столбец должен быть заполнен нулями.
    lvl - medium. Действовать будем следующим образом: сначала соберем множество всех индексов строк и стобцов
    в которых есть нули, а потом в цикле поменяем все строки и столбцы на строки и столбцы с нулями)
    '''
    rowSet, colSet = set(), set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rowSet.add(row)
                colSet.add(col)

    for i in rowSet:
        matrix[i] = [0 for _ in range(len(matrix[i]))]

    for j in colSet:
        for row in range(len(matrix)):
            matrix[row][j] = 0

    # print(*matrix, sep='\n')


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# setZeroes(matrix)
