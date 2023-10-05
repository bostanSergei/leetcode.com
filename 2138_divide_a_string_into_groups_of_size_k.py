def divideString(s: str, k: int, fill: str) -> list:
    '''
    :param s: строка, которую надо разделить над подстроки и закинуть в результирующий список
    :param k: длина каждой подстроки
    :param fill: заполнитель для последней подстроки при условии, если эта длина меньше чем k
    :return: вернуть итоговый список подстрок
    lvl - easy. Решим задачу прям в лоб. Циклом пробежимся по всей строке. В случае, если последний
    элемент будет меньше по длине чем требуется, добавим недостающий кусок.
    '''
    numItteration = len(s) // k + (1 if len(s) % k > 0 else 0)
    resultList = []
    for i in range(numItteration):
        resultList.append(s[i * k:i * k + k])

    if len(resultList[-1]) != k:
        resultList[-1] = resultList[-1] + fill * (k - len(resultList[-1]))

    return resultList


# s = "abcdefghij"
# k = 3
# fill = "x"
# print(divideString(s, k, fill))
