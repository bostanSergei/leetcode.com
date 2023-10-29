def canBeIncreasing(nums: list) -> bool:
    '''
    :param nums: список чисел
    :return: нужно проверить можно ли из этого спсиска сделать строго упорядоченный по возрастанию
    после одной единственной манипуляции: "извлечения" одного единственного числа из списка.
    True - если можно, False - если нельзя
    lvl - easy.
    '''
    for i in range(len(nums)):
        curLst = nums[:i] + nums[i+1:]
        if sorted(curLst) == curLst:
            if len(set(curLst)) == len(curLst):
                return True

    return False



# nums = [1, 2, 10, 5, 7]
nums = [2, 3, 1, 2]
print(canBeIncreasing(nums))
