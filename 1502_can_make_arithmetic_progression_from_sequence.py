def canMakeArithmeticProgression(arr):
    '''
    :param arr: список чисел (возможно неупорядоченный)
    :return: вернуть True если список является арифметической прогрессией
    lvl - easy, ну и тут всё просто. Одно из возможных решений: будем выяснять сколько возможных разностей
    между парами чисел существует. Если одна - прогрессия. Если больше - нет)
    '''
    resSet = set()
    arr.sort()
    for i in range(len(arr) - 1):
        resSet.add(arr[i + 1] - arr[i])
    return len(resSet) == 1


# arr = [1, 2, 3, 4]
# print(canMakeArithmeticProgression(arr))