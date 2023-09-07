def countEven(num):
    '''
    :param num: целое положительное число
    :return: вернуть количество чисел из диапазона от одного до num (включительно), которые удовлетворяют условию:
    сумма цифр числа должна быть четной) lvl - easy. Ну и тут пожалуй без комментариев)
    '''
    def evenNum(n):
        return sum([int(i) for i in str(n)]) % 2 == 0

    return sum([1 for i in range(1, num + 1) if evenNum(i)])


# num = 30
# print(countEven(num))