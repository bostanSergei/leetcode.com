def countPairs(nums, target):
    '''
    :param nums: список чисел
    :param target: целое число
    :return: нужно проверить все пары чисел (индекс первого числа должен быть обязательно меньше индекса
    второго числа) и сравнить сумму этих чисел с target. Если меньше - учтем эту пару в подсчете)
    lvl - easy
    '''
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1
    return count


# nums = [-6,2,5,-2,-7,-1,3]
# target = -2
# print(countPairs(nums, target))