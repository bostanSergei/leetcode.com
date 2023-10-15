from string import ascii_lowercase
from collections import Counter
from itertools import combinations


def maxScoreWords(words: list, letters: list, score: list) -> int:
    '''
    :param words: список слов, которые нужно будет составить из букв списком ниже
    :param letters: список букв. Буквы могут повторяться.
    :param score: 26 чисел. Каждое число - "стоимость" буквы латинского алфавита
    :return: вернуть максимально возможную стоимость слов (может быть одно или несколько), которые
    можно составить из данного количества букв. Смысл в том, что букв - ограниченное количество.
    LVL - HARD и я честно говоря, удивлен тому, что я не вылетел за time limit
    В целом, комментировать особо нечего. Решение сводится к тому, чтобы отсеять слова, которые
    мы не можем составить (букв не хватает), а после найти слова, которые можно использовать "вместе"
    для увеличения общей стоимости (не забывая при этом, что для составления двух-трех-четырех слов
    мы используем всё тот же ограниченный ресурс)
    '''
    symbolCost = {symbol: score[index] for index, symbol in enumerate(ascii_lowercase)}
    symbolCount = Counter(letters)

    resultList, maxScore = [], 0

    for word in words:
        currDict = Counter(word)
        if currDict <= symbolCount:
            currScore = sum([symbolCost[s] * count for s, count in currDict.items()])
            resultList.append((currScore, word))
            if currScore > maxScore:
                maxScore = currScore

    if maxScore == 0:
        return maxScore

    for i in range(2, len(resultList) + 1):
        currCombinations = combinations(resultList, r=i)
        for items in currCombinations:
            if Counter(''.join([tpl[1] for tpl in items])) <= symbolCount:
                currScore = sum([tpl[0] for tpl in items])
                if currScore > maxScore:
                    maxScore = currScore

    return maxScore


# words = ["dog", "cat", "dad", "good"]
# letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
# score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(maxScoreWords(words, letters, score))
