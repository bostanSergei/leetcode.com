def maximumTripletValue(nums: list) -> int:
    '''
    :param nums: список чисел.
    :return: Вернуть максимальное произведение (num[i] - num[j]) * k, в котором i, j, k - индексы списка, причем
    i строго меньше j, a j строго меньше k. lvl - medium.
    '''
    maxNum, result, maxDiff = 0, 0, 0

    for num in nums:
        result = max(result, maxDiff * num)
        maxDiff = max(maxDiff, maxNum - num)
        maxNum = max(maxNum, num)

    return result


nums = [12, 6, 1, 2, 7]
print(maximumTripletValue(nums))
