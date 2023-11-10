def majorityElement(nums: list) -> list:
    '''
    :param nums: список чисел, в котором нужно понять какие числв встречаются больше чем len(nums) / 3 раз
    :return: вернуть новый список чисел, удовлетворяющих условию.
    lvl - medium, но где тут medium я честно говоря не понял. Всего то надо составить словарь с числами в виде
    ключей, а в значения сохранять количество раз, которое то или иное число встречается. Далее еще раз пробежаться
    по словарю и забрать все ключи, удовлетворяющие условию.
    '''
    numsDict, count = {}, 0
    for num in nums:
        if num not in numsDict:
            numsDict[num] = 0
        numsDict[num] += 1

        count += 1

    resultList = []

    for key, val in numsDict.items():
        if val > count / 3:
            resultList.append(key)

    return resultList


# nums = [3, 2, 3]
# print(majorityElement(nums))
