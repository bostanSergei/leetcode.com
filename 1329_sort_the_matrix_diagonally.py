def diagonalSort(mat: list) -> list:
    '''
    :param mat: матрица, в которой необходимо отсортировать по возрастанию все диагонли
    :return: полученную матрицу
    lvl - medium. В общем, я тут, конечно, наворотил, но с задачей справился. Идея следующая. Сначала я собрал
    все стартовые индексы всех диагоналей: это левый столбец снизу вверх и верхняя строка справа налево.
    Далее я добавил к этим спискам все индексы всех диагоналей (стартовый индекс плюс 1 по строке и столбцу).
    В заключительной стадии отсортировал полученные списки (по значениям) и обновил данные в стартовой матрице.
    Задача интересная - стоит своего уровня)
    '''
    row, col = len(mat) - 1, len(mat[0]) - 1

    startIndexes = []
    while row >= 0:
        startIndexes.append([[row, 0, mat[row][0]]])
        row -= 1

    startCol, row = 1, len(mat) - 1
    while startCol <= col:
        startIndexes.append([[0, startCol, mat[0][startCol]]])
        startCol += 1

    for lst in startIndexes:
        iRow, iCol = lst[0][0], lst[0][1]
        while iRow < row and iCol < col:
            iRow += 1
            iCol += 1
            lst.append([iRow, iCol, mat[iRow][iCol]])

        copyList = [l.copy() for l in lst]

        lst.sort(key=lambda x: x[2])

        for i in range(len(copyList)):
            mat[copyList[i][0]][copyList[i][1]] = lst[i][2]

    return mat


# mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
# print(diagonalSort(mat))
