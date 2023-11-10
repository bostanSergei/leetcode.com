def searchMatrix(matrix: list, target: int) -> bool:
    '''
    :param matrix: матрица с размерами m на n. Причем все числа в строке и все числа в столбце идут по неубыванию.
    :param target: число, которое нужно найти в матрице.
    :return: Если цель поиска есть - вернуть истину. Иначе - false.
    Сделать все это нужно за минимальное время. Простой перебор в этой задаче не подойдет. Поэтому во первых при
    поиске числа в первую очередь будем смотреть на первый и последний элемент строки и если число в теории может
    быть в этой строке - будем применять бинарный поиск. Иначе - пропускать эту строку. lvl - medium
    '''
    flag, lenRow = False, len(matrix[0])

    for row in matrix:
        if row[-1] < target or row[0] > target:
            continue
        else:
            left, right = 0, lenRow - 1
            while left <= right:
                middle = (left + right) // 2
                if target in [row[left], row[middle], row[right]]:
                    return True

                elif row[middle] < target:
                    left = middle + 1
                elif row[middle] > target:
                    right = middle - 1

    return flag


# matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
# target = 5
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
print(searchMatrix(matrix, target))
