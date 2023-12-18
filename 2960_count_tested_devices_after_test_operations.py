def countTestedDevices(batteryPercentages: list) -> int:
    '''
    :param batteryPercentages: список батареек, которые нужно протестировать
    :return: количество успешных тестов
    lvl - easy. Суть в том, что тестить батарейку будем только в том случае, если её "заряд" больше нуля.
    И каждый раз, когда мы тестим батарейку, остальные уменьшаются в заряде на 1. Не стал ничего выдумывать)
    '''
    count = 0
    for index in range(len(batteryPercentages)):
        if batteryPercentages[index] > 0:
            count += 1
            batteryPercentages[index:] = [num - 1 for num in batteryPercentages[index:]]

    return count


# batteryPercentages = [1, 1, 2, 1, 3]
# print(countTestedDevices(batteryPercentages))
