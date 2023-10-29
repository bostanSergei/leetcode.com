def makeGood(s: str) -> str:
    '''
    :param s: строка, из которой нужно сделать красивую строку)
    :return: вернуть результат.
    Суть в следующем: если в строке есть одинаковых символа (подряд), но в разном регистре (например аА или Аа),
    то эти символы из строки нужно удалить. lvl - easy. Изначально было желание вспомнить регулярные выражения,
    но чет передумал, хотя решение могло быть очень красивым)
    '''
    flag = True
    while flag:
        lenStringBefore = len(s)
        symbolsList = []
        index = 0
        while index < lenStringBefore:
            if index + 1 != lenStringBefore:
                if s[index + 1].isupper() and s[index] == s[index + 1].lower():
                    symbolsList.append('')
                    index += 2
                elif s[index + 1].islower() and s[index] == s[index + 1].upper():
                    symbolsList.append('')
                    index += 2
                else:
                    symbolsList.append(s[index])
                    index += 1
            else:
                symbolsList.append(s[index])
                index += 1

        s = ''.join(symbolsList)
        lenStringAfter = len(s)
        if lenStringAfter == lenStringBefore:
            flag = False

    return s


# s = 'leEeetcode'
# print(makeGood(s))
