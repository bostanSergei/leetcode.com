def smallestEqual(nums):
    '''Мы должны пробежаться по индексам нашего списка чисел и проверить следующее:
    если индекс нашего элемента делится на 10 и в остатке получается число,
    раное nums[index], тогда вернем этот индекс и закончим цикл, так как индекс
    нам нужен наименьший. Если такого индекса мы не найдем, вернем -1'''
    resultIndex = 0
    for ind in range(len(nums)):
        if ind % 10 == nums[ind]:
            resultIndex = ind
            break
    return resultIndex




# for test
nums = [4, 3, 2, 1]
print(smallestEqual(nums))