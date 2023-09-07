def minStartValue(nums):
    '''
    :param nums: список чисел для которых необходимо вычислить минимальное стартовое значение
    :return: это значение должно быть такми, чтобы в процессе поэлементного сложения всех
    элементов массива сымма никогда бы не была меньше единицы
    lvl - easy, в целом без комментариев - задание достаточно простое
    '''
    minSum, start = 1, 0
    for i in nums:
        start += i
        if start < minSum:
            minSum = start

    return abs(minSum) + 1 if minSum <= 0 else minSum


nums = [1, -2, -3]
print(minStartValue(nums))