def validSquare(p1: list, p2: list, p3: list, p4: list) -> bool:
    points_list = [p1, p2, p3, p4]
    distance_list = []
    for i in range(4):
        curr_distance = []
        for j in range(4):
            if i == j:
                continue
            x1, y1, x2, y2 = points_list[i] + points_list[j]
            curr_distance.append(round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3))
        distance_list.append(tuple(sorted(curr_distance)))

    side = sum([i[0] + i[1] for i in distance_list]) / 8
    return len(set(distance_list)) == 1 and side == distance_list[0][0] and side > 0


# p1 = [0, 0]
# p2 = [1, 1]
# p3 = [1, 0]
# p4 = [0, 1]
# print(validSquare(p1, p2, p3, p4))
