def cellsInRange(s: str) -> list:
    '''
    :param s: в строке через ":" записаны две Excel ячейки: стартовая и конечная. Представим что мы выбрали их
    инструментом "выделение".
    :return: Нужно вернуть список всех ячеек, попадающих под наше "выделение"
    lvl - easy. В целом, перебираем, формируем, добавляем в список. Вроде, всё очень просто.
    '''
    startSymbol, startNumber = s[0], int(s[1])
    finishSymbol, finishNumber = s[3], int(s[4])
    resultList = []
    while startSymbol <= finishSymbol:
        for i in range(startNumber, finishNumber + 1):
            resultList.append(startSymbol + str(i))

        startSymbol = chr(ord(startSymbol) + 1)

    return resultList


# s = "A1:F1"
# print(cellsInRange(s))
