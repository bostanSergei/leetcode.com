def reverseWords(s: str) -> str:
    '''
    :param s: строка, в которой последнее слово нужно поставить на первое место, предпослднее на второе и так далее
    :return: вернуть новую строку
    lvl - medium и это максимально странно. Задача решается в пару строчек.
    Не буду выдумывать велосипед. split, reversed и join, хотя можно было и через while менять left и right местами
    '''
    lst = s.split()
    return ' '.join(reversed(lst))


s = "the sky is blue"
print(reverseWords(s))
