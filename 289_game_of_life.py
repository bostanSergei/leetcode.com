def gameOfLife(board: list) -> list:
    '''
    :param board: дана матрица (вложенный список) состоящая из нулей и единиц. Смысл в следующем. Нужно пройти
    по каждому элементу матрицы и в зависимости от условий описанных ниже, внести изменения в эту матрицу.
    Условия проверяем по исходной матрице (то есть анализуируя условную второую строку матрицы, мы должны опираться
    на наши знания о начальном состоянии матрицы (перед началом создаем глубокую копию)). Итак, условия:
    0 - мертвая клетка. 1 - живая клетка.
    Любая живая клетка, имеющая менее двух живых соседей, умирает.
    Любая живая клетка с двумя или тремя живыми соседями доживает до следующего поколения.
    Любая живая клетка, имеющая более трех живых соседей, погибает.
    Любая мертвая клетка, имеющая ровно три живых соседа, становится живой клеткой.
    :return: возвращать по условию задачи ничего не нужно. Меняем список на месте. Я добави return для проверок
    lvl - medium и пришлось прям разобраться, так как при первом написании алгоритма допустил довольно глупую
    ошибку на которую в последствии потратил много времени. Но не суть)
    В целом, задача сводится к сбору соседей для каждого элемента матрицы и их анализу с последующим изменением
    элемента для которого проводится анализ. Более, расписывать, пожалуй, нечего)
    '''
    boardCopy = [lst.copy() for lst in board]

    def createLst(m, n, i, j):
        indexList = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1],
                     [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
        resList = []
        for ind in indexList:
            if any([ind[0] < 0, ind[0] >= m, ind[1] < 0, ind[1] >= n]):
                continue
            else:
                resList.append(boardCopy[ind[0]][ind[1]])
        return resList

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            lst = createLst(m, n, i, j)
            if boardCopy[i][j] == 0 and lst.count(1) == 3:
                board[i][j] = 1
            elif boardCopy[i][j] == 1:
                if lst.count(1) > 3:
                    board[i][j] = 0
                elif lst.count(1) in [2, 3]:
                    continue
                elif lst.count(1) < 2:
                    board[i][j] = 0
    return board


# board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# board = [[0, 1, 0, 0, 1, 1, 0],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 0, 0, 0, 0, 1],
#          [1, 1, 0, 0, 1, 0, 0]]
# print(*gameOfLife(board), sep='\n')
