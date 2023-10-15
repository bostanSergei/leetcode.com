def checkString(s: str) -> bool:
    '''
    :param s: строка, в которой есть только символы 'a' и 'b'.
    :return: если все 'a' прописаны раньше, чем хоть одна из 'b', тогда вернуть True, иначе False
    '''
    indexA, indexB = -1, -1
    for i in range(len(s)):
        if s[i] == 'a':
            indexA = i
        if s[i] == 'b' and indexB == -1:
            indexB = i

    return indexB > indexA if indexB != -1 else True


# s = 'bbb'
# print(checkString(s))
