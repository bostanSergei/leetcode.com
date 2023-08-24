def intersection(nums):
    '''
    :param nums: вложенный список на вход
    :return: определить пересекающиеся элементы.
    easy lvl - решим через пересечение множеств. На выходе - отсортируем выдачу
    '''
    newSet = set(nums[0])
    for i in range(1, len(nums)):
        newSet &= set(nums[i])
    return sorted(newSet)



nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums))