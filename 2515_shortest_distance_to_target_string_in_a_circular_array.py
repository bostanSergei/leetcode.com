def closetTarget(words, target, startIndex) -> int:
    '''
    :param words: список слов в котором может находится target - цель-слово, которое мы ищем
    :param target: цель-слово)
    :param startIndex: индекс, с которого ночинается поиск
    :return: вернуть минимальную дистанцию до target'а от startIndex
    lvl - easy. Искать будем пос следующему принципу: снчала составим список индексов слов-целей.
    Если этот список окажется пустым или startIndex окажется в числе этих индексов - вернем или -1 или 0 соответственно.
    Если нет, посчитаем два возможных расстояния: вперед через последний элеменет к первому, и назад через первый
    к последнему. Далее посчитаем прямое расстояние между startIndex и индексами наших элементов, которые мы ищем
    и в итоге вернем минимальное расстояние из получившихся списков) В целом задача простая, но без листа бумаги не обошлось)
    '''
    l = len(words)
    indexList = [index for index in range(l) if words[index] == target]
    print(indexList)
    if len(indexList) == 0:
        return -1
    if startIndex in indexList:
        return 0
    secondList = []
    secondList.append(l - startIndex + indexList[0])
    secondList.append(l + startIndex - indexList[-1])
    indexList = [abs(index - startIndex) for index in indexList]

    return min(indexList + secondList)


# words = ["hello", "i", "am", "leetcode", "hello"]
# target = "hello"
# startIndex = 1
# words = ["hsdqinnoha", "mqhskgeqzr", "zemkwvqrww", "zemkwvqrww", "daljcrktje", "fghofclnwp", "djwdworyka", "cxfpybanhd",
#          "fghofclnwp", "fghofclnwp"]
# target = 'zemkwvqrww'
# startIndex = 8
# print(closetTarget(words, target, startIndex))
