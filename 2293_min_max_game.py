def minMaxGame(nums):
    '''
    :param nums: список чисел по которому нужно проиттерироваться парами, сравнивая числа между собой
    :return: вернуть наименьшее, которое будет выбрано в соответствии со следующим алгоритмом:
    из первой пары берем минимальное, из второй пары - максимальное, из третей минимальное, и так далее
    когда дойдем до условия, при котором у нас останется одно единственное число - вернум его.
    Пример: дан список [1, 3, 5, 2, 4, 8, 2, 2, 5] -> [[1, 3], [5, 2], [4, 8], [2, 2], [5]] ->
    -> [1, 5, 4, 2, 5] -> снова на пары -> [[1, 5], [4, 2], [5]] - > [1, 4, 5] -> [[1, 4], [5]] -> [1, 5] -> 1
    lvl - easy. В целом, ничего необычного. Классическая задача на циклы
    '''
    while len(nums) > 1:
        newNums = []
        for i in range(len(nums) // 2 + 1 if len(nums) % 2 == 1 else len(nums) // 2):
            if i % 2 == 0:
                newNums.append(min(nums[i * 2:(i + 1) * 2]))
            else:
                newNums.append(max(nums[i * 2:(i + 1) * 2]))
        nums = newNums
    return nums[0]


# nums = [93, 40]
# nums = [1, 3, 5, 2, 4, 8, 2, 2, 5]
# print(minMaxGame(nums))
