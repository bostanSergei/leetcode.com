def minimumRightShifts(nums):
    '''
    :param nums: список чисел (может быть как отсортирванный по неубыванию, так и нет)
    :return: вернуть количество сдвигов вправо, которые требуется сделать для того, чтобы саммив стал отсортированным,
    либо -1, если сделать этого не получится
    Что такое сдвиг вправо? допустим есть массив [3, 4, 5, 1, 2]. Сдвиг вправо это когда мы двойку перенесом в начало
    массива, то есть после первого сдвига мы получаем массив [2, 3, 4, 5, 1]. После второго - [1, 2, 3, 4, 5]
    Поскольку массив стал отсортированным - вернум двойки - количество раз.
    '''
    result = sorted(nums)
    if result == nums:
        return 0
    count = 1
    for i in range(-1, -len(nums), -1):
        if nums[i:] + nums[:i] == result:
            return count
        count += 1
    return -1

nums = [2, 1, 4]
print(minimumRightShifts(nums))