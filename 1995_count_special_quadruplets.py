def countQuadruplets(nums):
    '''
    :param nums: псисок чисел в котором нужно найти 4 числа, в которых сумма первых трех равна четвертому,
    причем индексы этих чисел должны распологаться в возрастающем порядке
    :return: количество таких "пар"
    '''
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        result += 1
    return result


nums = [1, 1, 1, 3, 5]
print(countQuadruplets(nums))
