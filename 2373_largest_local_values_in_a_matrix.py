def largestLocal(grid: list) -> list:
    n = len(grid)
    result_matrix = [[0] * (n - 2) for i in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            max_number = max(
                grid[i][j], grid[i][j + 1], grid[i][j + 2],
                grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2],
            )
            result_matrix[i][j] = max_number

    return result_matrix


# grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
# print(largestLocal(grid))
