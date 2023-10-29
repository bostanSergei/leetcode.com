def rearrangeCharacters(s: str, target: str) -> int:
    '''
    :param s: набор символов из которых нужно будет собрать target-слово
    :param target: само слово, которое нужно "собрать"
    :return: количество слов, которое получится собрать)
    lvl - easy. Соберем все в один словарь. Ключем будут символы target-слова, значением список, в котором первое
    значение - количество символов, необходимых для сборки одного target-слова, а вторым - количество символов
    в строке s. Вернуть нужно будет минимальное значение, полученного в результате целочисленного деления второго
    значения на первое. В целом, простая задача)
    '''
    targetDict = {}
    for symbol in target:
        if symbol not in targetDict:
            targetDict[symbol] = [0, 0]
        targetDict[symbol][0] += 1

    for symbol in s:
        if symbol in targetDict:
            targetDict[symbol][1] += 1

    resultList = [i[1] // i[0] for i in targetDict.values()]
    return min(resultList)


# s = "ilovecodingonleetcode"
# target = "code"
# s = "abbaccaddaeea"
# target = "aaaaa"
# print(rearrangeCharacters(s, target))
