from operator import *
from functools import reduce


def arraySign(nums):
    '''
    :param nums: дан список чисел. Нам нужно найти произведение всех чисел
    :return: и вернуть -1, 0 или 1 если результат меньше нуля, равен нулю или больше нуля
    я в свое время не очень хорошо понял функцию reduce, jпэтому самое время исправиться
    и вернуться к ней, чтоб разобраться. Вроде все работает)
    '''
    result = reduce(mul, nums)
    return 1 if result > 0 else 0 if result == 0 else -1


# nums = [-1,-2,-3,-4,3,2,1]
# print(arraySign(nums))