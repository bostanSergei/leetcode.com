def findSubarrays(nums):
    '''
    :param nums: список чисел, из которого нужно составить подсписки (по два числа)
    :return: вернуть True если существуют подсписки с одинаковой суммой чисел, иначе False
    lvl - easy. Можно немного улучшить данное решение, если на лету сравнивать сумму двух чисел
    и проверять есть ли полученное число в списке. Но решил так - влетаю в нормальный стат по времени
    '''
    newList = []
    for i in range(len(nums) - 1):
        newList.append(nums[i] + nums[i + 1])
    return len(newList) != len(set(newList))


# nums = [1, 2, 3, 4, 5]
# print(findSubarrays(nums))