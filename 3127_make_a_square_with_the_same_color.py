def canMakeSquare(grid: list) -> bool:
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            curr_sq = [
                grid[i][j],
                grid[i][j + 1],
                grid[i + 1][j],
                grid[i + 1][j + 1]
                ]
            curr_sq.sort()
            if curr_sq == ['B', 'B', 'B', 'W'] or curr_sq == ['B', 'W', 'W', 'W']:
                return True
            if len(set(curr_sq)) == 1:
                return True
    return False
