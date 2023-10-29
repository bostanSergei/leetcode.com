def minimumDifference(nums: list, k: int) -> int:
    '''
    :param nums: список чисел. Числа в списке - оценки студентов
    :param k: количество студентов, из которых нужно сформировать "группу"
    :return: минимальную разницу между самой высокой и самой низкой оценкой в группе
    lvl - easy. Сортируем список, бежим циклом по сриавниваем разницу крайних элементов.
    Задача - тривиальна и по сути не требует детальных объяснений)
    '''
    nums.sort()
    diff = nums[-1] - nums[0]

    for i in range(len(nums) - k + 1):
        if (cur := nums[i + k - 1] - nums[i]) < diff:
            diff = cur

    return diff


# nums = [9, 4, 1, 7]
# nums = [20980, 13353, 51423, 11920, 41836, 51586, 54445]
# k = 5
# print(minimumDifference(nums, k))
