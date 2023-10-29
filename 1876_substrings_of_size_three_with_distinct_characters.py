def countGoodSubstrings(s: str) -> int:
    '''
    :param s: строка символов
    :return: вернуть количество таких подстрок, длина которых равна трем и в подстроке нет повторяющихся символов
    lvl - easy. Для решения пробежимся циклом и для каждой подстроки будем проверять длину множества символов)
    '''
    count = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) == 3:
            count += 1
    return count


# s = "xyzzaz"
# print(countGoodSubstrings(s))
