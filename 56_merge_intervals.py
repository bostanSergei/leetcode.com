def merge(intervals: list):
    '''
    :param intervals: дан список списков, каждый элемент списка - список с двумя значениями [начало диапазона, конец диапазона]
    :return: вернуть итоговый список, в котором будут собраны воедино "пересекающиеся" диапазоны. То есть если рядом
    стоит два списка [[1, 3], [2, 6]] то из них нужно собрать один [1, 6] так как мы имеем то самое пересечение.
    Задача lvl - medium и я прям попотел, пока не понял логики и закономерностей. Решение собственно внизу)
    '''
    if len(intervals) == 1:
        return [intervals[0]]
    intervals.sort(key=lambda x: x[0])

    start, end = 0, 1

    resultIntervals, currInterval = [], intervals[0].copy()

    while end < len(intervals):
        if currInterval[1] >= intervals[end][0]:
            currInterval[1] = max(intervals[end][1], currInterval[1])
            end += 1
            continue
        else:
            resultIntervals.append(currInterval)
            currInterval = intervals[end]
            end += 1
    resultIntervals.append([currInterval[0], max(intervals[end - 1][1], currInterval[1])])

    return resultIntervals


# intervals = [[1, 4], [2, 3]]
# intervals = [[1, 4], [0, 2], [3, 5]]
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(merge(intervals))
