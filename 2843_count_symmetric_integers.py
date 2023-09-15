def countSymmetricIntegers(low, high):
    '''
    :param low: целое положительное число - начало диапазона
    :param high: целое положительное число - конец диапазона
    :return: вернуть количество симметричных чисел в указанном диапазоне
    число считается симметричным если сумма первой половины числа равно сумме второй половине числа
    Под суммой подразумевается сумма цифр числа. Число нечетной длины не может быть симметричным
    lvl - easy.
    '''
    count = 0
    for i in range(low, high + 1):
        center = len(str(i)) // 2 if len(str(i)) % 2 == 0 else 0
        if not center:
            continue
        lst = [int(j) for j in str(i)]
        if sum(lst[:center]) == sum(lst[center:]):
            count += 1
    return count


# low = 1
# high = 100
# print(countSymmetricIntegers(low, high))