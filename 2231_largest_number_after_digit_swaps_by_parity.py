def largestInteger(num: int) -> int:
    numsList = [int(i) for i in str(num)]
    odd_even_nums = [numsList[i] % 2 for i in range(len(numsList))]
    evenNums = sorted(filter(lambda x: x % 2 == 0, numsList), reverse=True)
    oddNums = sorted(filter(lambda x: x % 2 == 1, numsList), reverse=True)
    oddIndex = evenIndex = 0

    resultList = []
    for i in range(len(numsList)):
        if odd_even_nums[i] == 0:
            resultList.append(evenNums[evenIndex])
            evenIndex += 1
        else:
            resultList.append(oddNums[oddIndex])
            oddIndex += 1

    return int(''.join(map(str, resultList)))
