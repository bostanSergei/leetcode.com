def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> list:
    '''
    :param rows: количество строк в матрице
    :param cols: количество столбцов в матрице
    :param rCenter: икс для "центральной ячейки"
    :param cCenter: игрик для "центральной ячейки"
    :return: вернуть отсортированный список расстояний от каждой ячейки до центральной
    lvl - easy. условие задачи, честно говоря, написано очень запутанно. И как оказалось - суть решения - полный бред.
    По факту сводится к сортировке, так как автор задачи считает номальным заполнять матрицу набором значений [row, col],
    хотя в самой задаче речь идет про distance между ячейками. А при раскладе ниже, дистанция вычисляется не совсем
    корректно. К примеру, в тестах ниже автор считает что дистанция от [0, 1] в матрице 3 на 4 до [2, 3] составляет [2, 2].
    Две еденицы по X и две единицы по Y. В общем, на мой взгляд, правильней эту задачу решать по закоментированным
    строчкам, а не по логике автора.
    PS: матрица создана для понимания, из чего складывается 'ответ'. В решении, конечно она не нужна. Просто занимает память.
    '''
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    resultList = []

    for row in range(rows):
        for col in range(cols):
            # lst = [abs(rCenter - row), abs(cCenter - col)]
            lst = [row, col]
            # matrix[row][col] = lst
            resultList.append(lst)

    resultList.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

    # print(*matrix, sep='\n')
    # print()
    return resultList


# rows = 3
# cols = 4
# rCenter = 0
# cCenter = 0
# print(allCellsDistOrder(rows, cols, rCenter, cCenter))
