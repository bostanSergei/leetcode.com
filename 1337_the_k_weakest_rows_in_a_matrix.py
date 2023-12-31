def kWeakestRows(mat, k):
    '''
    :param mat: двумерный массив (матрица), элементами в которой выступают нули и единицы
    :param k: количество элементов, которые мы вернем на выход по заданному условию
    :return: чем больше в строке единиц - тем больше "вес" строки. Если в строках единиц
    одинаковое количество - сравниваем индексы этих строк. Нужно вернуть первые k-индексов
    в соответствии с указанным выше условием. lvl- easy
    '''
    resList = [[ind, sum(mat[ind])] for ind in range(len(mat))]
    sortedList = sorted(resList, key=lambda x: (x[1], x[0]))
    return [i[0] for i in sortedList][:k]


# mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
# k = 3
# print(kWeakestRows(mat, k))