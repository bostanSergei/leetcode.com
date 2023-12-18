def findWordsContaining(words: list, x: str) -> list:
    '''
    :param words: список слов в которых мы будем искать символ x
    :param x: тот самый символ, поиском которого мы будем заниматься
    :return: вернуть список индексов, где каждое значение - это индекс списка, в элементе которого содержится x
    Задача easy lvl - на разминочку с генератором списков. В целом, бех особых комментариев.
    '''
    resultList = [i for i in range(len(words)) if x in words[i]]

    return resultList


words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
print(findWordsContaining(words, x))
