def findIndices(nums: list, indexDifference: int, valueDifference: int) -> list:
    '''
    :param nums: список чисел
    :param indexDifference: минимально возможная разница между первым и вторым индексом чисел
    :param valueDifference: минимально возможная разница между первым и вторым значением
    :return: вернуть два возможных индекса, удовлетворяющие заданным условиям. Или [-1, -1] если таких чисел нет
    lvl - easy
    '''
    resultList = []
    for i in range(0, len(nums) - indexDifference):
        for j in range(i + indexDifference, len(nums)):
            if abs(nums[i] - nums[j]) >= valueDifference:
                resultList.append([i, j])

    print(resultList)
    if len(resultList) > 0:
        return resultList[0]
    return [-1, -1]


# nums = [11, 3, 36, 17, 13, 0, 26]
# indexDifference = 2
# valueDifference = 33
# print(findIndices(nums, indexDifference, valueDifference))
