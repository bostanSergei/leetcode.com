def reverseOnlyLetters(s):
    '''
    :param s: дана строка, которую нужно перевернуть. последний символ на место первого, предпоследний на место
    второго и тоак далее
    :return: НО, мы не должны трогать НЕалфавитные символы. То есть если есть строка типа 1234-5-67 где цифры
    это алфавитные символы, то мы должны вернуть строку 7654-3-21 то есть дифисы должны остаться на своих местах
    lvl - easy, решаем по принципу двух указателей
    '''
    start, end = 0, len(s) - 1
    resList = list(s)
    while start < len(s) and end > -1:
        if s[end].isalpha() and resList[start].isalpha():
            resList[start] = s[end]
            start += 1
            end -= 1
        elif not s[end].isalpha():
            end -= 1
        elif not resList[start].isalpha():
            start += 1
    return ''.join(resList)

#
# s = "a-bC-dEf-ghIj"
# print(reverseOnlyLetters(s))