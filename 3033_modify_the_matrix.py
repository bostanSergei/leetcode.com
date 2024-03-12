def modifiedMatrix(matrix: list) -> list:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                max_number = max(matrix[k][j] for k in range(len(matrix)))
                matrix[i][j] = max_number

    return matrix


# matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
# print(modifiedMatrix(matrix))
