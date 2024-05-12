def scoreOfString(s: str) -> int:
    score_list = list(map(ord, s))
    result = 0
    for i in range(len(score_list) - 1):
        result += abs(score_list[i] - score_list[i + 1])

    return result
