def lengthOfLongestSubstring(s: str) -> int:
    '''
    :param s: строка
    :return: вернуть максимальную длинну подстроки в которой все символы будут разными
    lvl - medium и я чет решил эту задачу очень сложно и очень плохо по времени. Но решение прошло, что уже
    не может не радовать. Схема описанная ниже думаю всем будет максимально понятна, я же пойду разбираться
    что там за решения с временем O(n)
    '''
    if s == '':
        return 0
    if len(set(s)) == 1:
        return 1

    maxSymbol, leftIndex, stringLen = 1, 0, len(s)
    while maxSymbol < stringLen - leftIndex and leftIndex < stringLen:
        for sIndex in range(leftIndex + 1, stringLen):
            curS = s[leftIndex:sIndex + 1]
            if len(curS) > len(set(curS)):
                break
            else:
                maxSymbol = max(maxSymbol, len(curS))
        leftIndex += 1

    return maxSymbol


# s = 'pwwkew'
# print(lengthOfLongestSubstring(s))
