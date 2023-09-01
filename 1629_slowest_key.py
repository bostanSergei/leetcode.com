def slowestKey(releaseTimes, keysPressed):
    '''
    :param releaseTimes: дан список с количеством секунд (если быть более точным, то список releaseTimes
    представляет из себя "таймлайн" (ноль отсутствует) в котором каждое число - это секунда в которую
    палец переносили с одной клавиши на другую (список клавиш в списке ниже)
    :param keysPressed: и список с кнопками, которые нажимали на клавиатуре.
    :return: Нужно вернуть кнопку, которая была нажата максимальное количество секунд
    Задача сложная в объяснении и простая в решении. lvl - easy
    '''
    resList = [0] * len(releaseTimes)
    for i in range(len(releaseTimes)):
        if i == 0:
            resList[i] = releaseTimes[i] - i
        else:
            resList[i] = releaseTimes[i] - releaseTimes[i - 1]
    symbol = ''
    maxNum = max(resList)
    for i in range(len(resList)):
        if resList[i] == maxNum and keysPressed[i] > symbol:
            symbol = keysPressed[i]
    return symbol


# releaseTimes = [12,23,36,46,62]
# keysPressed = "spuda"
# print(slowestKey(releaseTimes, keysPressed))