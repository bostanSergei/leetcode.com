def checkXMatrix(grid):
    '''
    :param grid: матрица с размером n * n
    :return: вернуть True если числа на главных и второстепенных диагоналях НЕ равны нули и если остальные
    числа равны нулю. Иначе  - False
    lvl - easy. Переберем циклом все значения и проверим условия принадлежности чисел к одно йиз групп)
    '''
    flag = True
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or (i + j) == n - 1:
                if grid[i][j] == 0:
                    flag = False
                    break
            else:
                if grid[i][j] != 0:
                    flag = False
                    break
        if not flag:
            break
    return flag


# grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# grid = [[5,7,0],[0,3,1],[0,5,0]]
# print(checkXMatrix(grid))