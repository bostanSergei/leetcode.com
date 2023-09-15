from itertools import groupby

def checkZeroOnes(s):
    '''
    :param s: дана строка, в которой содержатся нули и единицы
    :return: нужно поделить эту строку на подстроки (последовательность только единиц и только нулей),
    посчитать длину каждой последовательности и если самая длинная последовательность - единицы - вернуть
    true, иначе false
    lvl - easy и это самое подходящее время вспомнить itertools
    upd: runtime - лучше чем 90% решений)
    '''
    startList = groupby(s)
    resList = [[symb, len(list(obj))] for symb, obj in startList]
    resList.sort(key=lambda obj: [-obj[1], obj[0]])

    return True if resList[0][0] == '1' else False


s = "1110100010"
print(checkZeroOnes(s))