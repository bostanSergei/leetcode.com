def checkIfExist(arr):
    '''
    :param arr: список чисел
    :return: нужно проверить, есть ли в списке числа, удвоив которые мы получим другое число из этого же списка.
    Индексы чисел (стартового и удвоенного) должны быть разными
    '''
    flag = False
    for i in arr:
        for j in range(i + 1, len(arr)):
            if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                flag = True
                break
    return flag

#
# arr = [-2, 0, 10, -19, 4, 6, -8]
# print(checkIfExist(arr))
