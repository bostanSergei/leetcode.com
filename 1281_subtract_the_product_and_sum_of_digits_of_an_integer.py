from functools import reduce
from operator import mul, add


def subtractProductAndSum(n: int):
    '''
    :param n: Целое натуральное число
    :return: нужно вернуть разницу между произведением цифр числа и суммой цифр числа
    если на вход 123, то наша задача 1 * 2 * 3 - (1 + 2 + 3) = 0. вернем ноль)
    Задача easy lvl - попробуем вспомнить про reduce и operator (лишним точно не будет)
    '''
    numbersList = [int(i) for i in str(n)]
    prodNum = reduce(mul, numbersList)
    sumNum = reduce(add, numbersList)
    return prodNum - sumNum



# n = 234
# print(subtractProductAndSum(n))