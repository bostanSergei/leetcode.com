def sumIndicesWithKSetBits(nums, k):
    '''
    :param nums: список чисел
    :param k: количество бит, которые должны быть включены в каждом элементе
    :return: вернуть сумму чисел из списка входящих, в которых соблюдается условие равенства битности
    '''
    newDict = {index: sum([1 for i in bin(index)[2:] if i == '1']) for index in range(len(nums))}
    result = 0
    for j in range(len(nums)):
        if newDict[j] == k:
            result += nums[j]
    return result

nums = [5, 10, 1, 5, 2]
k = 1
print(sumIndicesWithKSetBits(nums, k))