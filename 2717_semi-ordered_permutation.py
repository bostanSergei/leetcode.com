def semiOrderedPermutation(nums):
    '''
    :param nums: список чисел, которые необходимо "отсортировать"
    :return: количество перестановок, необходимых для правильной "сортировки"
    Главная задача - получить на первом месте списка - единицу, а на последнем
    максимальное число списка, то есть двигать будем только эти два этих числа.
    Можно было подумать над математической "формулой", найти индексы этих чисел,
    и в одну строчку выдать ответ, но так интереснее. Подвигаем числа физически)
    '''
    count = 0
    while nums[0] != 1 or nums[-1] != len(nums):
        for i in range(1, len(nums)):
            if nums[i-1] in (1, len(nums)) or nums[i] in (1, len(nums)):
                if nums[i - 1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    count += 1
    return count

nums = [2, 4, 1, 3]
print(semiOrderedPermutation(nums))