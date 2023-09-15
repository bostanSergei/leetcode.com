from collections import Counter

def checkAlmostEquivalent(word1, word2):
    '''
    :param word1: набор символов
    :param word2: набор символов
    :return: если разница в количестве символов не превышает трех единиц - вернуть True, иначе False
    '''
    firstDict, secondDict, flag = Counter(word1), Counter(word2), True
    for symb in set(word1 + word2):
        if symb in firstDict and symb in secondDict:
            if abs(firstDict[symb] - secondDict[symb]) > 3:
                flag = False
        elif symb in firstDict and firstDict[symb] > 3:
            flag = False
        elif symb in secondDict and secondDict[symb] > 3:
            flag = False
        if not flag:
            break

    return flag


# word1 = "aaaa"
# word2 = "bccb"
# word1 = "abcdeef"
# word2 = "abaaacc"
# print(checkAlmostEquivalent(word1, word2))