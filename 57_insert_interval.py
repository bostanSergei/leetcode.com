def insert(intervals: list, newInterval: list) -> list:
    '''
    :param intervals: список списков, в котором каждый элемент - списко из двух значений: начало и конец интервала
    :param newInterval: список из двух значений: начало и конец нового интервала, который нужно "воткнуть" стартовый
    :return: вернуть результат
    Пример: при вставке [4, 8] в [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] нам нужно объеденить массивы
    [3, 5], [6, 7], [8, 10] в массив [3, 10], так как [4, 8] объединяет все эти массивы в один.
    На выходе получим [[1, 2], [3, 10], [12, 16]]
    lvl - medium. Решать будем с использованием стека)
    '''
    if len(intervals) == 0:
        return [newInterval]
    resultList = []
    currList = []
    for _ in range(len(intervals)):
        interval = intervals.pop(0)
        if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
            if len(currList) > 0:
                resultList.append(currList[:])
                currList.clear()
            resultList.append(interval)
        else:
            currList.append(min(interval[0], newInterval[0]))
            currList.append(max(interval[1], newInterval[1]))
    for i in range(len(resultList)):
        if len(resultList[i]) > 2:
            resultList[i] = [resultList[i][0], resultList[i][-1]]
    return resultList


# intervals = [[1, 3], [6, 9]]
# newInterval = [2, 5]

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

print(insert(intervals, newInterval))
