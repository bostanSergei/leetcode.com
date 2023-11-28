def floodFill(image: list, sr: int, sc: int, color: int) -> list:
    '''
    :param image: матрица заполненная числами
    :param sr: номер строки
    :param sc: номер столбца
    :param color: цифра, на которую нужно будет заменить все "подходящие" по условию значения из матрицы
    :return: вернуть итоговый результат
    В общем задача: посмотреть на число, которое стоит по указанному номеру строки и номкру столбца.
    Если элемент который стоит справа, слева, сверху или снизу равен исходному, то его мы тоже убдем
    менять на color. Точно такую же проверку нужно будет выполнить с этим же числом.
    lvl - easy. Задача - интересная и в целом не очень сложная. Возможно мое решение не самое оптимальное, но всё же)
    '''
    example = image[sr][sc]
    doneIndexList, queue = [[sr, sc]], [[sr, sc]]
    countRow, countCol = len(image), len(image[0])

    while queue:
        row, col = queue.pop()
        top = [row - 1, col] if row >= 1 else None
        right = [row, col + 1] if col <= countCol - 2 else None
        bottom = [row + 1, col] if row <= countRow - 2 else None
        left = [row, col - 1] if col >= 1 else None

        resultIndexList = [i for i in [top, right, bottom, left] if i is not None and image[i[0]][i[1]] == example]

        for indexes in resultIndexList:
            if indexes not in doneIndexList:
                queue.append(indexes)
                doneIndexList.append(indexes)

    for row, col in doneIndexList:
        image[row][col] = color

    return image


# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# sr = 1
# sc = 1
# color = 2
# print(floodFill(image, sr, sc, color))
