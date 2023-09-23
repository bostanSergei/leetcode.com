def furthestDistanceFromOrigin(moves):
    '''
    :param moves: строка на входе - движение по числовой прямой. Шаг влево - L, вправо - R, '_' - под вопросом
    :return: нужно вернуть расстояние на котором мы окажемся после всех n шагов, при условии что мы стремимся
    заменить '_' на L или R для того, чтобы "убежать" от начала координат максимально далеко)
    Простая задача easy lvl
    '''
    steps = sum(-1 if i == 'L' else 1 if i == 'R' else 0 for i in moves)
    numSpace = sum(1 for i in moves if i == '_')
    steps += numSpace if steps >= 0 else -numSpace
    return abs(steps)

# moves = "_______"
# print(furthestDistanceFromOrigin(moves))
