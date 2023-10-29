def percentageLetter(s: str, letter: str) -> int:
    '''
    :param s: строка (минимальной длины в 1 символ)
    :param letter: символ, который будем искать в строке
    :return: процент символов letter в строке
    lvl - easy. Не стал юзать стандартные len и count. Решил пробежать циклом и вернуть результат мат.операции
    '''
    stringLen, countSymbol = 0, 0

    for symbol in s:
        stringLen += 1
        if symbol == letter:
            countSymbol += 1

    return int((countSymbol / stringLen) * 100)
