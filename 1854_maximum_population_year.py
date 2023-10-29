def maximumPopulation(logs: list) -> int:
    '''
    :param logs: список, в котором элементами являются вложенные списки.
    Списки состоят из двух значений - год рождения и год смерти.
    :return: Вернуть год, в котором популяция была самой большой
    lvl - easy. Для решения задачи заведем словарь в котором ключами будут года: а значениями количество людей,
    которые в этот год жили. После этого отсортируем значения словаря по двум ключам: количество живущих на
    данный год людей и сам год. Вернем первое значение)
    '''
    populationDict = {}
    for start, end in logs:
        for year in range(start, end):
            if year not in populationDict:
                populationDict[year] = 0
            populationDict[year] += 1

    resultList = sorted([[year, population] for year, population in populationDict.items()],
                        key=lambda lst: (-lst[1], lst[0]))
    return resultList[0][0]


# logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
# print(maximumPopulation(logs))
