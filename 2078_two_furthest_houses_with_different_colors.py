def maxDistance(colors: list) -> int:
    '''
    :param colors: дан список чисел. Каждое число - это цвет дома, который стоит на прямой улице.
    :return: вернуть максимальное расстояние между домами разных цветов.
    lvl - easy. Задачу решим руководствуясь следующей логикой: сначало соберем в словарь индексы
    разных цветов так, чтоб ключем был цвет, а значением - список индексов, на позиции которых
    стоит дом. Ну а далее пробужим циклом по улице и для каждого дома вычислим максимум между
    домами разных уветов. Задача достаточно простая)
    '''
    colorsDict = {}
    for index in range(len(colors)):
        if colors[index] not in colorsDict:
            colorsDict[colors[index]] = []
        colorsDict[colors[index]].append(index)

    maxRange = 0
    for index in range(len(colors)):
        for key, value in colorsDict.items():
            if key != colors[index]:
                maxRange = max([maxRange, abs(index - max(value)), abs(index - min(value))])

    return maxRange


# colors = [1, 1, 1, 6, 1, 1, 1]
# colors = [1, 8, 3, 8, 3]
# print(maxDistance(colors))
