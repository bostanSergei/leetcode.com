def satisfiesConditions(grid: list) -> bool:
    flag = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i + 2 <= len(grid):
                if grid[i][j] != grid[i + 1][j]:
                    flag = False

            if j + 2 <= len(grid[i]):
                if grid[i][j] == grid[i][j + 1]:
                    flag = False

    return flag
