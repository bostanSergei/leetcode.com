def halvesAreAlike(s):
    '''
    :param s: строка, длина которой - четное число
    :return: нам нужно разделить строку на две части и проверить, является ли количество гласных символов
    одинаковым в обеих частях строки. Реализую проверку через генератор списков, проверяя вхождение каждого
    сивола в заранее объявленную переменную. В целом, задача easy lvl и по времени выполнения - в лидерах)
    '''
    symbols = 'aeiou'
    return [True for i in s[:len(s) // 2] if i.lower() in symbols] == [True for j in s[len(s) // 2:] if j.lower() in symbols]

#
# s = 'book'
# print(halvesAreAlike(s))