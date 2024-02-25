def uniqueOccurrences(arr: list) -> bool:
    '''
    :param arr: список чисел, часть из которых может повторяться.
    :return: вернуть True, если количество вхождений каждого элемента уникально
    lvl - easy. no comments
    '''
    uniqNumbers = set(arr)
    counterDict = {arr.count(num) for num in uniqNumbers}

    return len(uniqNumbers) == len(counterDict)
