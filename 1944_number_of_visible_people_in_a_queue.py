def canSeePersonsCount(heights: list) -> list:
    '''
    :param heights:
    :return:
    '''
    resultList = [0] * (len(heights) - 1)
    for i in range(len(heights) - 1, -1, -1):
        count = 0
        while i < len(heights) - 1:


            i += 1

        resultList[i] = count
heights = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights))
