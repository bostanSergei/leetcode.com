def sortColors(nums: list) -> None:
    '''
    :param nums: дан список чисел, состоящий из нулей, единиц и двоек
    :return: нужно отсортировать список без использования встроенных инструментов сортировки
    возвращать ничего не нужно. Изменяем изначальный список. lvl- medium. Реализую через словарь)
    '''
    colorsDict = {0: 0, 1: 0, 2: 0}
    for i in nums:
        colorsDict[i] += 1
    index = 0
    for key, val in colorsDict.items():
        while val > 0:
            nums[index] = key
            index += 1
            val -= 1


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
