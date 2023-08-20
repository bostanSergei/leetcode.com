def countPoints(rings: str):
    '''
    :param rings: на вход поступает строка в которой чередуются буквы R, B, G и цифры от 0 до 9 (позиции)
    :return: нужно вернуть количество позиций в которых есть сразу и R и G и B
    В общем смысл. Представьте что у вас есть 9 коробок, пронумерованных от 0 до 9ти. Мы двигаемся по строке
    B0R0G0R9R0B0G0 - первая пара символов B0 - это значит что мы в нулевую коробку закинем B (blue). Вторая
    пара символов R0 - в ту же нулевую коробку улетает R (red). Нуж вернуть количество коробок, в которой окажется
    сразу 3 цвета (red, blue, green). Задача максимально простая. Решим через словари
    '''
    newDict = {str(ind): set() for ind in range(10)}
    for i in range(0, len(rings), 2):
        newDict[rings[i + 1]].add(rings[i])
    return len([1 for key, val in newDict.items() if len(val) == 3])


# rings = "B0B6G0R6R0R6G9"
# print(countPoints(rings))