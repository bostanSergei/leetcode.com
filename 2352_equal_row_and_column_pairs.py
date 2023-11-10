def equalPairs(grid: list) -> int:
    '''
    :param grid: матрица с размером N x N (размер матрицы не задан)
    :return: нужно вернуть количество пар (строк / столбцов), которые являются идентичыми
    lvl - medium. Задача, простая на первый взгляд, однако с первого захода я уперся в тупик (как всегда на time limit).
    В итоге, правильным решением считаю подсчет пар через словари, где ключем является кортеж очередной строки, а
    значением - количество таких строк. На втором проходе мы будем использовать полученные данные, выполняя иттерцию
    уже по столбцам натрицы, что в кончегом итоге и придедет нас к правильному ответу.
    '''
    gridDict = {}
    for i in range(len(grid)):
        row = tuple(grid[i])
        if row not in gridDict:
            gridDict[row] = 0
        gridDict[row] += 1

    result = 0
    for j in range(len(grid)):
        col = tuple([grid[k][j] for k in range(len(grid))])
        if col in gridDict:
            result += gridDict[col]

    return result


grid = [[13, 13], [13, 13]]
print(equalPairs(grid))
