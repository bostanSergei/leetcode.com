def makeSmallestPalindrome(s: str) -> str:
    '''
    :param s: строка, из которой нужно сделать палиндром, при этом главным критерием по выбору заменящего символа
    будет лексографический порядок символов, то есть при строке abccbd мы доджны будем получить abccba, так как a < z)
    :return: вернуть итоговую строку
    lvl - easy. Задача достаточно простая. Два указателя, сравнение символов, замена на наименьший в случае расхождений
    '''
    left, right = 0, len(s) - 1
    wordList = list(s)
    while left < right:
        if wordList[left] != wordList[right]:
            symbol = min(wordList[left], wordList[right])
            wordList[left] = wordList[right] = symbol
        left += 1
        right -= 1
    return ''.join(wordList)


# s = "seven"
# print(makeSmallestPalindrome(s))
