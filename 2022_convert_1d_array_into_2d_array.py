def construct2DArray(original: list, m: int, n: int) -> list:
    if m * n != len(original):
        return []

    index = 0
    matrix = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = original[index]
            index += 1

    return matrix


# original = [1,2,3,4]
# m = 2
# n = 2
# print(construct2DArray(original, m, n))
