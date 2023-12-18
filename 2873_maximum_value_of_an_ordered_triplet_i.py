def maximumTripletValue(nums: list) -> int:
    '''
    :param nums: список чисел.
    :return: Вернуть максимальное произведение (num[i] - num[j]) * k, в котором i, j, k - индексы списка, причем
    i строго меньше j, a j строго меньше k. lvl - easy. Задачи уровня easy по классике решаем перебором.
    '''
    maxNum = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                curRes = (nums[i] - nums[j]) * nums[k]
                if curRes > maxNum:
                    maxNum = curRes

    return maxNum


nums = [12, 6, 1, 2, 7]
print(maximumTripletValue(nums))
