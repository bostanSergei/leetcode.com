def averageValue(nums: list) -> int:
    '''
    :param nums:
    :return:
    '''
    resSum, count = 0, 0
    for num in nums:
        if num % 3 == 0 and num % 2 == 0 and num > 0:
            resSum += num
            count += 1

    return round(resSum / count) if count > 0 else 0


nums = [9, 3, 8, 4, 2, 5, 3, 8, 6, 1]
print(averageValue(nums))
