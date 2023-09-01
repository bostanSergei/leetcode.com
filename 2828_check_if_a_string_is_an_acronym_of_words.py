def isAcronym(words, s):
    '''
    :param words: список слов. Из каждого слова нужно взять первую букву
    :param s: и сравнить со вловом из второго аргумента
    :return: true or false
    lvl - easy, адже комментировать нечего)
    '''
    return ''.join([i[0] for i in words]) == s