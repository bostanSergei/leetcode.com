from collections import Counter
def productExceptSelf(nums):
    '''
    level: medium
    :param nums: спсиок целых чисел
    :return: нужно вернуть список чисел, каждый элемент которого равен произведению
    всех чисел в списке, за исключением того числа, индекс которого мы вычисляем в
    настоящий момент времени. То есть если есть список чисел [1, 2, 3, 4], то
    res[0] = 2 * 3 * 4, res[1] = 1 * 3 * 4, res[2] = 1 * 2 * 4, res[3] = 1 * 2 * 3
    Нам предлагают решить задачу без использования знака деления.
    Я пойду нестандартным способом и решу задачу через counter, который на каждой
    иттерации буду перебирать генератом списков. Не очень хорошая ассимптотика, но
    это первое что пришло в голову)
    '''
    counterDict = Counter(nums)
    print(counterDict)
    resList = []
    for i in range(len(nums)):
        resList.insert(i, 1)
        copyDict = counterDict.copy()
        copyDict[nums[i]] -= 1
        newList = [key ** val for key, val in copyDict.items() if val != 0]
        for j in newList:
            resList[i] *= j
    return resList


# for test
# nums = [5, 9, 2, -9, -9, -7, -8, 7, -9, 10]
# print(len(nums))
# nums = [-1,1,0,-3,3]
# nums = [1, 2, 3, 4]
# print(productExceptSelf(nums))