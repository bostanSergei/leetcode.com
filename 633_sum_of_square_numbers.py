def judgeSquareSum(c: int) -> bool:
    square_set = set()
    for i in range(1, int((2 ** 31) ** 0.5) + 1):
        square_set.add(i ** 2)

    for num in square_set:
        if c - num in square_set:
            return True

    return False
