def luckyNumbers(matrix):
    '''
    :param matrix: двумерная матрица
    :return: вернуть элементы матрицы, которые будут являться самыми минимальными в строке и максимальными в столбце
    lvl - easy. Чтобы не искоть масимальный и максимальный на для каждого элемента, сделаем это заранее, пробежавшись
    по строкам и столбцам и сохраним это в список. Далее остается перебрать все элементы матрицы и сравнить их
    отношение к заранее сформированным спискам rowList и colList
    '''
    rowList, colList = [], []
    for i in range(len(matrix)):
        rowList.append(min(matrix[i]))
    for j in range(len(matrix[0])):
        colList.append(max([matrix[k][j] for k in range(len(matrix))]))

    resultList = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if rowList[i] == colList[j]:
                resultList.append(rowList[i])

    return resultList


# matrix = [[3, 7, 8],
#           [9, 11, 13],
#           [15, 16, 17]]
# matrix = [[1, 10, 4, 2],
#           [9, 3, 8, 7],
#           [15, 16, 17, 12]]
# print(luckyNumbers(matrix))
