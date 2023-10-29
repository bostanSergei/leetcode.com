def countLargestGroup(n: int) -> int:
    '''
    :param n: целое число
    :return: СЛОЖНА ОБЪЯСНИТЬ))) видимо поэтому у задачи больше дизлайлов, чем лайков) Но я попробую:
    в общем есть число 13. Нужно взять диапазон чисел от 1 до 13 (включительно) и посчитать сумму цифр этого числа
    1 -> 1          По суммам нам и нужно           1, 10
    2 -> 2          группировать числа              2, 11
    3 -> 3          То есть группы будут            3, 12
    4 -> 4          выглядеть так:                  4, 13
    5 -> 5                                          5
    6 -> 6                                          6
    7 -> 7                                          7
    8 -> 8                                          8
    9 -> 9                                          9
    10 -> 1
    11 -> 2                 Теперь задача сводится к тому, чтобы посмотреть, какая группа самая большая по количеству
    12 -> 3                 чисел (в нашем случае это группа с количесвтом чисел равным двум).
    13 -> 4                 Далее необходимо посчитать количество этих групп. В нашем случае - 4 группы. Возвращаем 4
    Задача lvl easy - решение сразу приходит после того, как понимаешь, что именно нужно сделать.
    '''
    numberDict = {}
    maxGroup = 0
    for num in range(1, n + 1):
        result = sum([int(j) for j in str(num)])
        if result not in numberDict:
            numberDict[result] = 0
        numberDict[result] += 1

        if numberDict[result] > maxGroup:
            maxGroup = numberDict[result]

    count = 0
    for value in numberDict.values():
        if value == maxGroup:
            count += 1

    return count


# n = 13
# print(countLargestGroup(n))
