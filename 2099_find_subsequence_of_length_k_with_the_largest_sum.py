def maxSubsequence(nums: list, k: int) -> list:
    '''
    :param nums: список чисел
    :param k: количество чисел, которое нужно взять из списка для нахождения максимальной суммы
    :return: список чисел, которые мы будем использовать при нахождении максимальной суммы. Причем в том же порядке,
    как в изначальном спсиске.
    lvl - easy, по сути нужно вытащить k-последних чисел из отсортированного списка, что я собственно и делаю ниже)
    '''
    numsList = [[index, nums[index]] for index in range(len(nums))]
    numsList.sort(key=lambda x: x[1])
    indexList = sorted([lst[0] for lst in numsList[-k:]])
    return [nums[index] for index in indexList]



# nums = [2, 1, 3, 3]
# k = 2
# print(maxSubsequence(nums, k))
