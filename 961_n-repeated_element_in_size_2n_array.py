from collections import Counter

def repeatedNTimes(nums):
    '''
    :param nums: список чисел
    :return: вернуть число которое повторяется в изначальном списке len(nums) // 2
    Для это подгружаем счетчик Counter и бежим по нему циклом, сравнивая ключ с нашим
    исходным значением
    '''
    pass
    newDict = Counter(nums)
    whatTimes = len(nums) // 2
    for key, val in newDict.items():
        if val == whatTimes:
            return key


# for test:
# nums = [1,2,3,3]
# print(repeatedNTimes(nums))