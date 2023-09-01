def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    '''
    :param numOnes: количество единиц в "запасе"
    :param numZeros: количество нулей в "запасе"
    :param numNegOnes: количество минус единиц в "запасе"
    :return: вернуть максимальную сумму, которую мы можем собрать из имеющихся чисел
    lvl - easy. Решим через срез одного большого списка общих чисел
    '''
    resList = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
    return sum(resList[:k])


# numOnes = 3
# numZeros = 2
# numNegOnes = 0
# k = 2
# print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))