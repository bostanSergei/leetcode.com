def dailyTemperatures(temperatures: list) -> list:
    '''
    :param temperatures: список целых чисел, где каждый элемент температура в i-ый день
    :return: нужно вернуть список, в которм каждый элемент будет представлен в виде целого числа: количества
    дней до первого дня, когда температура будет выше чем сегодня (в текущем элементе).
    lvl - medium. Долго сидел с задачей) Написал минимум три алгоритма - последний прошел (остальные падали по времени)
    Логику в двух словах описать сложно: но пробежавшись по коду можно понять что там происходит.
    Кроме того, решил оставить первую версию кода: время выполнения страдает, но почему бы и нет)
    '''
    temperatureDict, tempLen = {}, len(temperatures)

    resultList = [0 for i in range(tempLen)]

    for i in range(tempLen - 1, -1, -1):
        if temperatures[i] not in temperatureDict:
            temperatureDict[temperatures[i]] = []

        temperatureDict[temperatures[i]].append(i)

        if i == tempLen - 1:
            continue

        if temperatures[i] == temperatures[i + 1] and resultList[i + 1] != 0:
            resultList[i] = resultList[i + 1] + 1
        elif temperatures[i] == temperatures[i + 1] and resultList[i + 1] == 0:
            continue

        else:
            currTemp = temperatures[i] + 1
            currList = []
            while currTemp < 101:
                if currTemp in temperatureDict:
                    currList.append(temperatureDict[currTemp][-1] - i)
                currTemp += 1
            if len(currList) > 0:
                resultList[i] = min(currList)

    return resultList



    # tempDict = {temp: [] for temp in range(30, 101)}
    #
    # for i in range(len(temperatures)):
    #     tempDict[temperatures[i]].append(i)
    #
    # # for key in tempDict.copy():
    # #     if len(tempDict[key]) == 0:
    # #         del tempDict[key]
    #
    # resultList = []
    #
    # # print(tempDict)
    #
    # for index in range(len(temperatures)):
    #     keysList = [key for key in tempDict.keys() if key > temperatures[index]]
    #     # print(keysList)
    #     indexList = []
    #     for key in keysList:
    #         indexList.extend([i for i in tempDict[key] if i > index])
    #
    #     print(indexList)
    #
    #     indexList.sort()
    #     if len(indexList) > 0:
    #         resultList.append(min(indexList) - index)
    #     else:
    #         resultList.append(0)
    #
    # return resultList



temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))
