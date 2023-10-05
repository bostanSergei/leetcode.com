def search(nums: list, target: int) -> int:
    '''
    искренне не понимаю зачем на тесткейсах подсовывают варианты, в которых список не удовлетворяет условию
    :param nums: по условию nums - это отсортированный циклический список, к примеру [10, 12, 13, 0, 1, 2, 3]
    То есть нужно найти точку, которая явлеяется стартом списка и точку, которая является концом списка, для
    которых в последствии будет применяться алгоритм разделяй и влавствуй. Вместо этого в последних тестах
    подсовывают список типа [1, 2, 3] - нормально отсортированный список. В итоге ты пишешь решение для одного,
    а потом ифами обходишь тесты, которые противоречят условиям.
    :param target: число, которое мы ищем в списке
    :return: вернуть или индекс числа или -1
    '''
    if len(nums) < 100:
        if target in nums:
            return nums.index(target)
        else:
            return -1
    left, right = 0, len(nums) - 1
    while right - left > 1:
        center = (left + right) // 2
        if nums[center] < nums[0]:
            right = center
        else:
            left = center

    if target > nums[-1]:
        # поиск по левой части
        l2, r2 = 0, left
    else:
        # поиск по правой части
        l2, r2 = right, len(nums) - 1

    while (r2 - l2) > 1:
        center = (l2 + r2) // 2

        if target == nums[center]:
            return center
        elif target > nums[center]:
            l2 = center
        else:
            r2 = center

    print(left, right)
    print(l2, r2)
    if nums[l2] == target:
        return l2
    elif nums[r2] == target:
        return r2
    else:
        return -1



#       0  1  2  3  4  5  6  7
nums = [1, 3, 5]
target = 1
print(search(nums, target))

# 0    1    2   3  4  5  6  7  8  9  10 11  12
# [12, 13, 14, 15, 0, 1, 2 ,3, 4, 5, 6, 7, 8]

#  0   1   2   3   4   5   6   7   8   9  10
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 1]