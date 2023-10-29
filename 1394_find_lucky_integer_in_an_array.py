def findLucky(arr: list) -> int:
    '''
    :param arr: список целых чисел
    :return: вернуть максимально счастливое число. Число является счастливым если количество этих чисел в массиве
    равно самому числу. lvl - easy. Классика на словари без особых комментариев)
    '''
    newDict = {}
    for i in arr:
        if i not in newDict:
            newDict[i] = 0
        newDict[i] += 1

    resultList = []
    for key, val in newDict.items():
        if key == val:
            resultList.append(key)

    return -1 if len(resultList) == 0 else max(resultList)
