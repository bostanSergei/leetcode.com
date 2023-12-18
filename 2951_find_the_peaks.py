def findPeaks(mountain: list) -> list:
    '''
    :param mountain:
    :return:
    lvl - easy и тут без комментариев
    '''
    resultList = []
    for i in range(1, len(mountain) - 1):
        if mountain[i - 1] < mountain[i] > mountain[i + 1]:
            resultList.append(i)

    return resultList
