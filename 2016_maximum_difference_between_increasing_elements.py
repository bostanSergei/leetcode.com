def maximumDifference(nums: list) -> int:
    '''
    :param nums: список чисел
    :return: нужно максимально возможную разницу между двумя элементами списка. При это индекс первого числа
    должен быть меньше индекса второго. lvl - easy. Вложенный цикл и погнали) Можно было отсортировать
    элементы с учетом их индексов в изначальном списке, но я пошел по протаренной дорожке)
    '''
    result = -1
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] < nums[j] and (diff := (nums[j] - nums[i])) > result:
                result = diff

    return result


# nums = [7, 1, 5, 4]
# nums = [1, 5, 2, 10]
# print(maximumDifference(nums))
