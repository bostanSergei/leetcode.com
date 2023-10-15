def findFinalValue(nums: list, original: int) -> int:
    '''
    :param nums: список чисел
    :param original: стартовое число. Задача: проверить есть ли число в списке. Если есть, умножить на 2 и повторить процедуру)
    :return: вернуть итоговое число)
    lvl - easy. Чет прям совсем easy
    '''
    while original in nums:
        original *= 2
    return original


# nums = [5, 3, 6, 1, 12]
# original = 3
# print(findFinalValue(nums, original))
