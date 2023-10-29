def stringMatching(words: list) -> list:
    '''
    :param words: список слов
    :return: вернуть новый список, который состоит из тех слов, которые являются подстроками других слов из списка
    lvl - easy. Думал как решить задачу с чуть лучшей асимптотикой, в итоге сдал решение с вложенным циклом, и
    получил результат по runTime улчше чем у 97% всех отправленных решений. Удивительно)
    '''
    resultList = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                if words[i] not in resultList:
                    resultList.append(words[i])

    return resultList


# words = ["mass", "as", "hero", "superhero"]
# print(stringMatching(words))
