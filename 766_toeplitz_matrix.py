def isToeplitzMatrix(matrix: list) -> bool:
    max_x, max_y = len(matrix) - 1, len(matrix[0]) - 1
    # diagonals_list = []
    for i in range(max_y + 1):
        cur_set = set()
        cur_pos = 0
        while i <= max_y and cur_pos <= max_x:
            cur_set.add(matrix[cur_pos][i])
            cur_pos += 1
            i += 1

        if len(cur_set) > 1:
            return False
        # diagonals_list.append(cur_set)

    for i in range(max_x + 1):
        cur_set = set()
        cur_pos = 0
        while i <= max_x and cur_pos <= max_y:
            cur_set.add(matrix[i][cur_pos])
            cur_pos += 1
            i += 1

        if len(cur_set) > 1:
            return False
        # diagonals_list.append(cur_set)

    return True


# matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# print(isToeplitzMatrix(matrix))
