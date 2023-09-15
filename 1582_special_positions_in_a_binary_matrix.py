def numSpecial(mat):
    '''
    :param mat: дана матрица, заполненная нулями и единицами
    :return: вернуть количество "особенных элементов". Особенным считается элемент равный единице, у которого в
    строке и в столбце больше нет единиц.
    lvl - easy, чтоб не вычислять количество единиц в строках и столбцах на каждой иттерации, сначала создам
    два словаря, а далее уже пробежимся по всем элементам матрицы)
    '''
    rowDict = {index: sum(mat[index]) for index in range((len(mat)))}
    colDict = {index: sum([mat[i][index] for i in range(len(mat))]) for index in range(len(mat[0]))}
    result = 0

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1 and rowDict[i] + colDict[j] == 2:
                result += 1
    return result


# mat = [[1,0,0],[0,0,1],[1,0,0]]
# mat = [[1,0,0],[0,1,0],[0,0,1]]
# mat = [[0, 0, 1, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 1, 0, 0]]
# print(numSpecial(mat))