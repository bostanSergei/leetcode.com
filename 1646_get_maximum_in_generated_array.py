def getMaximumGenerated(n: int) -> int:
    if n == 0:
        return 0
    startList = [0, 1]
    for i in range(2, n + 1):
        curr_index = i // 2
        if i % 2 == 0:
            startList.append(startList[curr_index])
        else:
            startList.append(startList[curr_index] + startList[curr_index + 1])

    print(startList)
    return max(startList)
