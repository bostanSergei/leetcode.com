def bestHand(ranks: list, suits: list) -> str:
    '''
    :param ranks: номинал карт из колоды
    :param suits: масть карт из колоды)
    :return: вернуть комбинацию, которую можно составить из текущих карт. Комбинаций 4: или флэш или три карты
    одного номинала или пара или старшая карта. lvl - easy. в целом решение - тривиально и не требует комметариев
    '''
    if len(set(suits)) == 1:
        return 'Flush'
    kardsDict = {}
    for i in ranks:
        if i not in kardsDict:
            kardsDict[i] = 0
        kardsDict[i] += 1
    maxKard = max(kardsDict.values())

    return 'Three of a Kind' if maxKard >= 3 else 'Pair' if maxKard == 2 else 'High Card'


# ranks = [13, 2, 3, 1, 9]
# suits = ["a", "a", "a", "a", "a"]
# ranks = [4, 4, 2, 4, 4]
# suits = ["d", "a", "a", "b", "c"]
# print(bestHand(ranks, suits))
