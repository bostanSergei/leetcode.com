def divisorSubstrings(num: int, k: int) -> int:
    '''
    :param num: целое число, с которым будем производить основные манипуляции
    :param k: число, которое характеризует "длину" чисел, на которые будем разбивать соновное число (длина подстроки)
    :return: вернуть количество делителей. Считаем следующим образом. Берем "подстроку" числа и пытаемся на эту подстроку
    поделить основное число. Если в итоге получаем ноль: добавляем единицу)
    lvl - easy. В целом, условия более чем достаточно для понимания дальнейших манипуляций
    '''
    num_format_to_string = str(num)
    count = 0
    for i in range(len(num_format_to_string) - k + 1):
        divisor = int(num_format_to_string[i:i + k])
        if divisor and num % divisor == 0:
            count += 1

    return count


# num = 430043
# k = 2
# print(divisorSubstrings(num, k))
