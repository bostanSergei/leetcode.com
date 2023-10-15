def trimMean(arr: list) -> float:
    '''
    :param arr: список целых положительных чисел
    :return: вернуть среднее арифметическое после одной простой манипуляции.
    Из списка нужно выбросить 5% самых больших чисел и 5% самых маленьких чисел.
    lvl - easy. По условию размер массива чисел кратен 20
    '''
    arr.sort()
    countNum = len(arr)
    resultLength = countNum * 0.9
    resultSum = sum(arr[countNum // 20:-countNum // 20])

    return resultSum / resultLength


# arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
# print(trimMean(arr))
