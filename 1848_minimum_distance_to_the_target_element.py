def getMinDistance(nums, target, start):
    '''
    :param nums: список чисел
    :param target: число, которое должно быть в списке чисел и индекс которого нам нужно найти. Число может быть не одно
    :param start: число, которое будем использовать для вычисления по формуле abs(i - start), где i - индексы target'ов
    :return: вернуть минимальную разницу между индексами и значением start
    Решаем через генератор списков, сформировав список индексов цели target в списке nums, а затем через тот же
    генератор формуриуем список возможных вариантов модулей разницы, вернув при этом самое минимальное значение
    '''
    targetIndexes = [i for i in range(len(nums)) if nums[i] == target]
    startIndexes = [abs(j - start) for j in targetIndexes]
    return min(startIndexes)



nums = [1,2,3,4,5]
target = 5
start = 3
print(getMinDistance(nums, target, start))