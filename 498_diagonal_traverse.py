def findDiagonalOrder(mat: list) -> list:
    '''
    :param mat: дана матрица размерами n * m
    :return: нужно вернуть одномерный массив, записанный путем чтения исходной матрицы по диагонали (вверх,
    по диагонали вниз, по диагонали вверх и так далее) lvl - medium
    '''
    maxRow, maxCol = len(mat), len(mat[0])
    currRow, currCol, elements = 0, 0, 0
    resultMatrix, target = [], 'up'
    while elements < maxRow * maxCol:
        resultMatrix.append(mat[currRow][currCol])
        if target == 'up':
            if currRow == 0 and currCol < maxCol - 1:
                currCol += 1
                target = 'down'
            elif currCol == maxCol - 1:
                currRow += 1
                target = 'down'
            else:
                currCol += 1
                currRow -= 1
        elif target == 'down':
            if currCol == 0 and currRow < maxRow - 1:
                currRow += 1
                target = 'up'
            elif currRow == maxRow - 1:
                currCol += 1
                target = 'up'
            else:
                currCol -= 1
                currRow += 1

        elements += 1
    return resultMatrix


# mat = [[1, 2], [3, 4]]
# print(findDiagonalOrder(mat))
