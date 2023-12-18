def isPrefixString(s: str, words: list) -> bool:
    '''
    :param s: дана строка, которую нужно получить путем добавления строк из списка.
    :param words: список, который будет использоваться для получения исходной строки.
    :return: True, если получить строку можно, False, если нет.
    lvl - easy, в целом без особых комментариев)
    '''
    resString, lenS = '', len(s)
    for word in words:
        resString += word
        if s == resString:
            return True
        elif len(resString) > lenS:
            return False

    return False
