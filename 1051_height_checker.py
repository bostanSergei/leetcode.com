def heightChecker(heights):
    '''
    :param heights: ученики, которые выстроились в ряд для школьной фотографии
    :return: вернуть количество учеников, которые встали не не свои места (стоять
    они должны по росту от меньшего к большему).
    Собственно создадим "правильный" список и сравним их)
    '''
    resultList = sorted(heights)
    return sum([1 for i in range(len(heights)) if heights[i] != resultList[i]])

#
# heights = [1,1,4,2,1,3]
# print(heightChecker(heights))