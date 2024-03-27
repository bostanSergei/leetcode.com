def minimumBoxes(apple: list, capacity: list) -> int:
    capacity.sort(reverse=True)
    all_apple, index_box = sum(apple), 0
    while all_apple > 0:
        all_apple -= capacity[index_box]
        index_box += 1

    return index_box


# apple = [5, 5, 5]
# capacity = [2, 4, 2, 7]
# print(minimumBoxes(apple, capacity))
