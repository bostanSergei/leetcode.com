def mergeSimilarItems(items1, items2):
    '''
    :param items1: дано два списка (вложенные)
    :param items2: каждый вложенный список представлен двумя элементами: уникальный "ключ" и значение
    :return: вернуть один общий вложенный список в котором будет представлена сумма значений по совпадающим ключам
    lvl - easy. Создадим словарь, в котором посчитаем сумму всех уникальных ключей, а далее сформируем итоговый
    список, отсортированный по ключам. В целом, достаточно простая задача.
    '''
    newDict = {}
    for el in items1 + items2:
        if el[0] not in newDict:
            newDict[el[0]] = el[1]
        else:
            newDict[el[0]] += el[1]
    return sorted([list(tpl) for tpl in newDict.items()])


# items1 = [[1, 1], [4, 5], [3, 8]]
# items2 = [[3, 1], [1, 5]]
# print(mergeSimilarItems(items1, items2))
