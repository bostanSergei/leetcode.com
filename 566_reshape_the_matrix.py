def matrixReshape(mat: list, r: int, c: int) -> list:
    row, col = len(mat), len(mat[0])
    count_elements = row * col
    if count_elements != r * c:
        return mat

    new_matrix = [[0] * c for i in range(r)]
    new_row, new_col = 0, 0
    for i in range(row):
        for j in range(col):
            new_matrix[new_row][new_col] = mat[i][j]
            new_col += 1
            if new_col == c:
                new_row += 1
                new_col = 0

    return new_matrix


mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(matrixReshape(mat, r, c))
