def canFormArray(arr: list, pieces: list) -> bool:
    '''
    :param arr: массив целых чисел (одномерный)
    :param pieces: двумерный массив, элеметами вложенного массива являются целые числа.
    :return: Нужно ответить на вопрос: можно ли, "раскрывая скобки" массивов pieces получить массив arr.
    То есть имея массив [[78], [4, 64], [91]] мы можем раскрыть его в массив [91, 78, 4, 64] (к примеру),
    НО НЕ можем расскрыть в массив [91, 64, 4, 78], так как изначально числа 64 и 4 стоят в другом порядке
    lvl - easy. Простая задача, не требующая комментариев.
    '''
    startIndex = 0
    while startIndex < len(arr):
        for secondLvlIndex in range(len(pieces)):
            if arr[startIndex] == pieces[secondLvlIndex][0]:
                if arr[startIndex:startIndex + len(pieces[secondLvlIndex])] == pieces[secondLvlIndex]:
                    startIndex += len(pieces[secondLvlIndex])
                    break
        else:
            return False
    return True


# arr = [91, 4, 64, 78]
# pieces = [[78], [4, 64], [91]]
# print(canFormArray(arr, pieces))
