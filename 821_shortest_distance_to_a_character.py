def shortestToChar(s, c):
    '''
    :param s: строка
    :param c: символ
    :return: вернуть список чисел, длина которого будет равна длине строки, а каждое число будет
    ближайшим расстоянием от текущего индекса слова до симвода, указанного в переменной c
    '''
    resultList = []
    indexList = [index for index, symbol in enumerate(s) if symbol == c]
    for i in range(len(s)):
        resultList.append(min([abs(i - j) for j in indexList]))

    return resultList





# for test
# s = "loveleetcode"
# c = "e"
# print(shortestToChar(s, c))