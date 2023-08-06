def maximumUnits(boxTypes: list, truckSize: int):
    '''
    :param boxTypes: Вложенные списки, где каждый элемент это список с двумя значениями:
    количество коробок на "палете" и количество "элементов" в коробке
    :param truckSize: максимальное количество коробок, которое вмещается в грузовик
    :return: нужно вернуть максимальное количество "элементов", которое можем засунуть в грузовик

    Задача максимально простая. Сортируем списки с помощью лямбда функции по второму значению от
    большего к меньшему и начинаем набирать коробки до тех пор, пока не дойдем до максимальной вместимости
    '''
    boxTypes.sort(key=lambda x: -x[1])
    print(boxTypes)
    result = 0
    index = 0
    while truckSize > 0 and index < len(boxTypes):
        if truckSize - boxTypes[index][0] >= 0:
            result += boxTypes[index][0] * boxTypes[index][1]
            truckSize -= boxTypes[index][0]
        elif truckSize - boxTypes[index][0] < 0:
            result += truckSize * boxTypes[index][1]
            truckSize = 0
        index += 1

    return result

# for test
# boxTypes = [[5,10],[2,5],[4,7],[3,9]]
# truckSize = 10
# print(maximumUnits(boxTypes, truckSize))