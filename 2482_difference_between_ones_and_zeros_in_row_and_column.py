def onesMinusZeros(grid):
    '''
    :param grid: двумерная матрица (количесвто строк может быть не равно количеству столбцов). Матрица состоит из единиц и нулей
    :return: нужно вренуть новую матрицу, в которой мы будем придерживаться следующего правила:
    каждый новый элемент это сумма всех единиц из текущего ряда ПЛЮС сумма всех единиц из текущего столбца МИНУС
    количество нулей из текущего ряда МИНУС количество нулей из текущего столбца.
    lvl - medium
    первое решение - в лоб - не прошло по времени выполнения. Функция вычисления каждого результата осталась в качестве
    заккоментированного кода. Далее было принято решение заранее посчитать значения для единиц для кадой строки и каждого
    столбца а после использовать полученные значения в последующих вычислениях. Что собственно и привело к успеху)
    '''
    # def result(row, col):
    #     onesRow = sum([1 for i in grid[row] if i == 1])
    #     zeroRow = len(grid[row]) - onesRow
    #     onesCol = sum([1 for j in grid if j[col] == 1])
    #     zeroCol = len(grid) - onesCol
    #     return onesRow + onesCol - zeroRow - zeroCol

    numRow, numCol = len(grid), len(grid[0])

    cashOnes = {'row': {}, 'col': {}}
    for i in range(numRow):
        cashOnes['row'][i] = sum([1 for j in grid[i] if j == 1])
    for i in range(numCol):
        cashOnes['col'][i] = sum([1 for j in grid if j[i] == 1])

    resultMatrix = [[0] * len(grid[0]) for i in range(len(grid))]
    for i in range(len(resultMatrix)):
        for j in range(len(resultMatrix[i])):
            resultMatrix[i][j] = cashOnes['row'][i] + cashOnes['col'][j] - (numRow - cashOnes['row'][i]) - (numCol - cashOnes['col'][j])
    return resultMatrix


# grid = [[1,1,1],[1,1,1]]
# grid = [[0,1,1],[1,0,1],[0,0,1]]
# print(onesMinusZeros(grid))