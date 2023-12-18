def divideArray(nums: list, k: int) -> list:
    '''
    :param nums: дан список чисел.
    :param k: и целое число.
    :return: задача разбить список на подсписки таким образом, чтобы каждый подписок был длиной в 3 элемента
    и разница между этими элементами не превышала значение k. Задача lvl medium, хотя на medium, честно говоря,
    она не тянет. Алгоритм достаточно простой и надежный)
    '''
    nums.sort()
    resultList = []
    for index in range(0, len(nums), 3):
        if nums[index + 2] - nums[index] <= k:
            resultList.append(nums[index:index + 3])
        else:
            return []

    return resultList


# nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
# k = 2
# print(divideArray(nums, k))
