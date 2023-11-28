def getSumAbsoluteDifferences(nums: list) -> list:
    '''
    :param nums: отсортированный по неубыванию список целых чисел.
    :return: сумму абсолютных разниц списка
    Допустим есть список [2, 3, 5]. Из этого списка мы получим [4, 3, 5]. логика следующая:
    result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4
    result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3
    result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5
    lvl - medium. На базовом цикле в цикле тут не проедешь - упремся в лимиты по времени. Все таки длина
    списка может быть очень большой. Вместо этого мы будем представим список в виде возрастающего графика,
    для которого нам потребуется вычислять площадь всего того что было до рассматриваемого элемента и после.
    Получив результаты по двум промежуточным спискам, мы сможем посчитать финальный - он и будет ответом.
    Была похожая задача на яндекс алгоритмах буквально месяц назад.
    '''
    lenList = len(nums)

    firstList = []
    s1, count1 = 0, 1
    for i in range(lenList):
        firstList.append(count1 * nums[i] - s1)
        s1 += nums[i]
        count1 += 1

    secondList = []
    s2, count2 = 0, 1
    for j in range(lenList - 1, -1, -1):
        secondList.append(s2 - count2 * nums[j])
        s2 += nums[j]
        count2 += 1

    secondList.reverse()

    for k in range(lenList):
        firstList[k] = abs(secondList[k] + firstList[k])

    return firstList


# nums = [2,3,5]
# nums = [1, 4, 6, 8, 10]
# print(getSumAbsoluteDifferences(nums))
