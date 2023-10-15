def nearestValidPoint(x: int, y: int, points: list) -> int:
    '''
    :param x: координата x
    :param y: координата y
    :param points: точки на плоскости
    :return: вернуть индекс самой близкой по расстоянию точки из списка точек
    lvl - easy. Условие следующее: расстояние до точки мы можем посчитать только в том случае, если или координата x
    или координата y
    '''
    distanceList = []
    for index in range(len(points)):
        if x == points[index][0] or y == points[index][1]:
            distance = abs(x - points[index][0]) + abs(y - points[index][1])
            distanceList.append([distance, index])

    if not len(distanceList):
        return -1

    distanceList.sort(key=lambda lst: (lst[0], lst[1]))
    return distanceList[0][1]


# x = 3
# y = 4
# points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
# print(nearestValidPoint(x, y, points))
