def maximalSquare(matrix: list) -> int:
    '''
    :param matrix: дана матрица, в которой элементами ясляются строки: единицы и нули
    :return: нужно найти площадь масого большого квадрата, Квадратом считается область в которой вся площадь
    заполнена единицами.
    lvl - medium. Задача решется путем динамического программирования. Создаем стартовую матрицу и начиаем
    перебираать все значения нашей стартовой, заполняя результирующую.
    '''
    rowLen, colLen = len(matrix), len(matrix[0])
    dp = [[0] * colLen for row in range(rowLen)]

    maxSize = 0

    for i in range(rowLen):
        for j in range(colLen):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                maxSize = max(maxSize, dp[i][j])

    return maxSize ** 2


# matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# print(maximalSquare(matrix))
