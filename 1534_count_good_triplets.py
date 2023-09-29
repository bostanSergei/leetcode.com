def countGoodTriplets(arr, a, b, c):
    '''
    :param arr: массив чисел
    :param a, b, c - числа, которые принимают участие в сравнении разности элементов из массива
    :return: количество "троек чисел", которые удовлетворяют следующему условию:
    индексы i < j < k, модуль разниц ((arr[i], arr[j]), (arr[j], arr[k]) и (arr[i], arr[k])) должен быть
    меньше a, b, c соответственно. lvl - easy. Для более менее нормального run time будем применять лайфхак:
    на последний цикл хазодить только в случае, если первое условие проходит - иначе игнорируем.
    '''
    count = 0

    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, len(arr)):
                    if all([abs(arr[j] - arr[k]) <= b, abs(arr[i] - arr[k]) <= c]):
                        count += 1

    return count


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))
print()
