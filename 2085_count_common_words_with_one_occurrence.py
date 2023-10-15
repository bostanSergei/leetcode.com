def countWords(words1: list, words2: list) -> int:
    '''
    :param words1, :param words2 список слов
    :return: нужно выяснить количесвто слов, которые есть и в первом и во втором списках и количество которых равно одному
    lvl - easy. Решим через словари. Задача на самом деле тривиальная.
    '''
    firstDict = {}
    secondDict = {}
    for i in words1:
        if i not in firstDict:
            firstDict[i] = 0
        firstDict[i] += 1
    for j in words2:
        if j not in secondDict:
            secondDict[j] = 0
        secondDict[j] += 1

    if len(firstDict) < len(secondDict):
        firstDict, secondDict = secondDict, firstDict
    result = 0
    for word, value in firstDict.items():
        if value == 1 and word in secondDict and secondDict[word] == 1:
            result += 1

    return result



# words1 = ["leetcode", "is", "amazing", "as", "is"]
# words2 = ["amazing", "leetcode", "is"]
# print(countWords(words1, words2))
