from collections import Counter

def firstUniqChar(s):
    '''
    :param s: дана строка
    :return: нужно вернсть индекс первого уникального символа в этой строке. Сделаем из строки Counter
    и начнем двигаться циклом по исходной строке, проверяя, чем является значение очередного индекса.
    Единице? Сразу вернем найденный индекс или -1 есди цикл закончится не провалившись в условие ни разу
    lvl - easy
    '''
    newDict = Counter(s)
    for index, symbol in enumerate(s):
        if newDict[symbol] == 1:
            return index
    return -1


#
# s = 'loveleetcode'
# print(firstUniqChar(s))