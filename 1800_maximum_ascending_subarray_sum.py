def maxAscendingSum(nums: list) -> int:
    '''
    :param nums: список чисел
    :return: вернуть сумму максимальной подпоследовательности, в которой каждое следующее число будет
    больше предыдущего. lvl - easy.
    '''
    if len(nums) == 1:
        return nums[0]

    maxSum, curSum = 0, 0
    for i in range(len(nums) - 1):

        curSum += nums[i]
        maxSum = max(maxSum, curSum)
        if nums[i] < nums[i + 1]:
            continue
        else:
            curSum = 0

    if nums[i] < nums[i + 1]:
        maxSum = max(maxSum, curSum + nums[i + 1])

    return maxSum
