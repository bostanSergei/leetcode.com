def rotate(nums, k):
    '''
    :param nums: список чисел
    :param k: целое число: количество раз, которое необходимо провернуть оперцию по "переворачиванию массива".
    Под операцией переворачивания подразумевается перестановка элемента из конца массива в начало массива.
    :return: Ничего не возвращаем. Тестовая система проверяет стартовый массив на соответствие.
    lvl - medium
    '''
    numsLen = len(nums)
    if k > numsLen:
        k = k % numsLen
    lst = []
    for i in range(k):
        lst.insert(0, nums.pop())
    nums[:] = lst + nums
    return None


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# print(rotate(nums, k))
#
# nums = [-1, -100, 3, 99]
# k = 2
# print(rotate(nums, k))
