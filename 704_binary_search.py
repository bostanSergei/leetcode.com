def search(nums: list, target: int) -> int:
    '''
    :param nums: список чисел
    :param target: число, которое требуется найти
    :return: реализовать классический бинарный поиск
    lvl - easy, алгоритм расписан во всех учебниках, поэтому без комментариев)
    '''
    left, right = 0, len(nums)
    while abs(left - right) > 1:
        center = (left + right) // 2
        if nums[center] == target:
            return center
        elif nums[center] < target:
            left = center
        else:
            right = center

    numbersList = [nums[left], nums[right]]
    if target in numbersList:
        index = numbersList.index(target)
        return left if index == 0 else right

    return -1
