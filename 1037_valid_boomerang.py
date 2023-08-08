import convert_name


def isBoomerang(points):
    '''
    :param points: список трех точек с координатами x, y
    :return: True - если точки не лежат на одной прямой, иначе False
    решать будем через площадь. Постараемся найти площадь фигуры, образованной
    после соединения точек. Если площадь больше 0, то точки не лажат на одной линии
    '''
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    S = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return S != 0


# for test
# points = [[1,1],[2,3],[3,2]]
# points = [[1,1],[2,2],[3,3]]
# print(isBoomerang(points))