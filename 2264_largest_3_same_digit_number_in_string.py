def largestGoodInteger(num: str) -> str:
    '''
    :param num:
    :return:
    '''
    resultList = []
    for i in range(1, len(num) - 1):
        if len(set(num[i-1:i+2])) == 1:
            resultList.append(num[i] * 3)

    if len(resultList) == 0:
        return ''
    resultList.sort()
    return resultList[-1]
