def countOperations(num1: int, num2: int) -> int:
    '''
    :param num1, num2: два целых числа
    :return: вернуть количество операций после которых одно из чисел достигнет нуля.
    Суть операции: от большего (первого) числа отнять меньшее (второе). Результат станет первым числом. Повторить процедуру
    Задача lvl - easy - решил в лоб. Пытался понять, как делить числа друг на друга (возможно через НОД), но в голову не пришло
    '''
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 < num2:
            num1, num2 = num2, num1
        num1, num2 = num1 - num2, num2
        count += 1
    return count

# num1 = 79
# num2 = 68
# print(countOperations(num1, num2))
