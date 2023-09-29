def canBeEqual(s1, s2):
    '''
    :param s1: дано два слова длиной 4 символа
    :param s2:
    :return: вернуть true если переставив символы с позициями "через один" можно получить из первого слова второе
    Пример: есть последовательность ABCD. Символ A мы можем переставить только с символом C, а символ B только с D,
    так как разница между двумя индексами состовляет две единицы. lvl - easy
    '''
    return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])


s1 = "abcd"
s2 = "dacb"
print(canBeEqual(s1, s2))