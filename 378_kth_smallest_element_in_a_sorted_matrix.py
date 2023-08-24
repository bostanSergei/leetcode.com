def kthSmallest(matrix, k):
    '''
    :param matrix: на вход матрица m * n
    :param k: порядковый номер числа, который стоит вернуть
    :return: нужно сформировать итоговый список (распаковать матрицу), отсортировать числа в порядке возрастания
    и потом уже вернуть число по счету k.
    lvl - medium. время решения этой задачи решением ниже - одно из самых быстрых, что немного
    странно, так как я сначала пытался придумать что-то такое из ряда вон выходящее, но потом пошел
    по классическому пути, в итоге получив runtime лучше чем у 99 процентов решивших
    '''
    newList = []
    for i in matrix:
        newList.extend(i)
    newList.sort()
    return newList[k - 1]


# matrix = [[1,5,9],[10,11,13],[12,13,15]]
# k = 6
# print(kthSmallest(matrix, k))