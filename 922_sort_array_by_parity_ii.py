def sortArrayByParityII(nums):
    '''
    :param nums: список чисел четной длины в котором количество четных и нечетных чисел равно
    :return: вернуть список где на каждом четном индексе будет стоять четное число, а на каждом нечетном - нечетное
    решим задачу через filter и zip) lvl - easy
    '''
    evenNums = filter(lambda x: x % 2 == 0, nums)
    oddNums = filter(lambda x: x % 2 == 1, nums)
    resList = []
    for pair in zip(evenNums, oddNums):
        resList.extend(pair)
    return resList


# nums = [4, 2, 5, 7]
# print(sortArrayByParityII(nums))