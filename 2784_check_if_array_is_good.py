def isGood(nums):
    '''
    :param nums: дан список чисел. Нужно проверить является ли он "хорошим"
    :return: true или false
    Предположим, есть длина массива, которая равна 5. Хорошим будет список:
    [1, 2, 3, 4, 4] - то есть это такой спсиок, который начинается с единицы
    и заканчивается числом n - 1 причем n - 1 повторяется в массиве 2 раза
    '''
    goodNums = list(range(1, len(nums))) + [len(nums) - 1]
    return sorted(nums) == goodNums


# for test
# nums = [2, 1, 3]
# print(isGood(nums))