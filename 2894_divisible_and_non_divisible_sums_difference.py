def differenceOfSums(n: int, m: int) -> int:
    '''
    :param n: целое число, из которого в процессе формируем диапазон [1, n + 1]
    :param m: целое число, на которое будем делить каждое число из диапазона, чтоб составить две суммы:
    числа которые деляться на m и числа которые НЕ делятся на m
    :return: вернуть разницу между второй суммой и первой
    lvl - easy. Простая тривиальная задача на цикл
    '''
    firstNum = 0
    secondNum = 0
    for i in range(1, n + 1):
        if i % m == 0:
            firstNum += i
        else:
            secondNum += i

    return secondNum - firstNum


# n = 10
# m = 3
# print(differenceOfSums(n, m))
