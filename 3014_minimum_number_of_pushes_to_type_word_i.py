def minimumPushes(word: str) -> int:
    '''
    :param word:
    :return:
    '''
    symbolDict = {}
    for symbol in word:
        if symbol not in symbolDict:
            symbolDict[symbol] = 0
        symbolDict[symbol] += 1

    symbolsList = [[val, key] for key, val in symbolDict.items()]
    symbolsList.sort(key=lambda lst: -lst[0])

    number_of_pushes = 0
    print(symbolsList)

    for i in range(len(symbolsList) // 8 + 1):
        for j in symbolsList[i * 8:(i + 1) * 8]:
            number_of_pushes += (i + 1) * j[0]

    return number_of_pushes

word = "xycdefghij"
print(minimumPushes(word))
