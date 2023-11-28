def lastVisitedIntegers(words: list) -> list:
    '''
    :param words: список строк. Строки могут быть представлены либо целыми числами, либо словом "prev"
    :return: вернуть список целых чисел, руководствуясь следующим правилом: если встречается "prev" - задача добавить
    в итоговый список последнее число, которое мы встретили до этого. Если "prev" встречатеся дважды / трижды (и тд)
    то нам требуется вернуть последнее, предпоследнее, пред-предпоследнее число (и тд). Если чисел "до" не было или
    они закончились, то вернуть нужно -1. То есть в списке [1, 2, "prev", "prev", "prev"] нужно будет вернуть [2, 1, -1],
    а в списке ["prev", 1, 2, "prev", "prev", "prev"] вернем [-1, 2, 1, -1]. В общем, количество возвращаемых элементов
    итогового списка будет равна количеству "prev" в стартовом списке, опираясь при этом на числа (и их порядок) из
    стартового списка. lvl - easy. Ждал в задаче подвохов, так как количество дизлайков очень сильно опережает количество
    лайков. Оказалось куда проще - решение прошло с первого запуска)
    '''
    numbersList, resultList, curIndex = [], [], -1

    for num in words:
        if num.isdigit():
            numbersList.append(int(num))
            curIndex = len(numbersList) - 1
        else:
            if curIndex > -1:
                resultList.append(numbersList[curIndex])
                curIndex -= 1
            else:
                resultList.append(-1)

    return resultList


# words = ["1", "2", "prev", "prev", "prev"]
# words = ["1", "prev", "2", "prev", "prev"]
# print(lastVisitedIntegers(words))