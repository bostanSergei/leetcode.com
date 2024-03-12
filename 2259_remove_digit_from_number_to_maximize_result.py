def removeDigit(number: str, digit: str) -> str:
    startList = [number] * len(number)
    for i in range(len(number)):
        if number[i] == digit:
            startList[i] = number[:i] + number[i + 1:]

    resultList = sorted(map(int, filter(lambda x: x != number, startList)))
    return str(resultList[-1])


# number = [['123', '3'], ['1231', '1'], ['551', '5']]
# for i, j in number:
#     print(removeDigit(i, j))
