def maxLengthBetweenEqualCharacters(s):
    '''
    :param s: дана строка, в которой могут быть одинаковые символы
    :return: нужно вернуть максимальное количество символов между двумя одинаковыми символами
    классика с двумя циклами, lvl - easy
    '''
    maxLen = -1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i - 1) > maxLen:
                maxLen = j - i - 1
    return maxLen


# s = 'abca'
s = 'aa'
print(maxLengthBetweenEqualCharacters(s))