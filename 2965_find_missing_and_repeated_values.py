def findMissingAndRepeatedValues(grid: list) -> list:
    '''
    :param grid: дана матрица N на N с числами от 1 до N ** 2
    :return: вернуть список из двух элементов в котором первый элемент встречается в матрице 2 раза,
    а второй элемент не встречается ни разу. lvl - easy.
    '''
    lenGrid, resultList = len(grid), [0, 0]
    numbersDict = {key: 0 for key in range(lenGrid ** 2 + 1)}
    for i in range(lenGrid):
        for j in range(lenGrid):
            numbersDict[grid[i][j]] += 1

    for key, value in numbersDict.items():
        if value == 2:
            resultList[0] = key
        elif value == 0:
            resultList[1] = key

    return resultList


# grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
# print(findMissingAndRepeatedValues(grid))
