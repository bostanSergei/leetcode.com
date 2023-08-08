def minDeletionSize(strs):
    '''
    :param strs: список строк одинаковой длины
    :return: количество столбцов (считай как число символо в одной строке (будет меньше или равно
    количеству символов в однйо строке)), которое не удовлетворяет условию, по которому столбцы
    должны быть отсортированы. Представим что у нас есть список ["cba","daf","ghi"]. Запишем его иначе:
    c   b   a   Получаем столбцы c-d-g, b-a-h И a-f-i
    d   a   f   Первый и последний идут в лексографческом порядке. Второй - нет
    g   h   i   Как итог - вернем 1 - количество столбцов, не удовлетворяюзих условию
    '''
    newList = list(''.join(strs))
    count = 0
    for i in range(len(strs[0])):
        newWord = newList[i::len(strs[0])]
        if newWord != sorted(newWord):
            count += 1

    return count


# for test
# strs = ["cba","daf","ghi"]
# print(minDeletionSize(strs))