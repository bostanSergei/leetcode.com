def reconstructQueue(people: list) -> list:
    '''
    :param people:
    :return:
    '''
    peopleDict = {}
    for p in people:
        if p[1] not in peopleDict:
            peopleDict[p[1]] = []
        peopleDict[p[1]].append(p[0])

    print(peopleDict)


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
