from itertools import combinations

def unequalTriplets(nums):
    '''
    :param nums: список чисел
    :return: вернуть количество уникальных трипл-коллекций (подсписков, состоящих из уникальных элементов)
    решу двумя способами: классический перебор через вложенные циклы for и через функцию combinations
    из модуля itertools. Решения по асимптоматике примерно одинаковые, поэтому принципиального прироста
    в скорости мы не увидим. Небольшым плюсом будет, если мы ручками будем сравнивать значения в подсписках,
    а не переводить их в set, но опять таки - прибавка в скорости не очень большая
    '''
    result = 0
    newList = list(combinations(nums, r=3))
    for i in newList:
        if i[0] != i[1] and i[1] != i[2] and i[2] != i[0]:
            result += 1
    return result

    # result = 0
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         for k in range(j + 1, len(nums)):
    #             if len(set([nums[i], nums[j], nums[k]])) == 3:
    #                 result += 1
    # return result

# nums = [4,4,2,4,3]
# print(unequalTriplets(nums))