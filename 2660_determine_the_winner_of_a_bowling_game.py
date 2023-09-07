def isWinner(player1, player2):
    '''
    :param player1: список кеглей, которые игрок 1 сбивает на i-ом ходе в игре в боулинг
    :param player2: список кеглей, которые игрок 2 сбивает на i-ом ходе в игре в боулинг
    :return: вернуть номер игрока который победил по очкам или 0 если очки одинаковые)
    lvl - easy, но задача проста только на первый взгляд. Если не вчитываться в условие, то можно упасть
    в ошибку на самых первых тестах. В общем суть: есть у игрока В ОДНОМ ИЗ ДВУХ прошлых ходов было выбито
    10 кеглей, то текщее количество кеглей нужно умножить на 2 и добавить к общему счету полученное количество
    очков. Иначе - без умножения. Короче, если у игрока список [10, 2, 2, 5], то его счет будет
    (10 * 1) + (2 * 2) + (2 * 2) + (5 * 1) так как удваиваться будут только второй и третий ход, а пятый не будет!
    В общем невнимательность привела к ошибкам на первых решениях)
    '''
    firstPlayerScore, secondPlayerScore = 0, 0
    for i in range(len(player1)):
        if (i > 1 and 10 in player1[i - 2:i]) or (i == 1 and player1[0] == 10):
            firstPlayerFlag = 2
        else:
            firstPlayerFlag = 1

        if (i > 1 and 10 in player2[i - 2:i]) or (i == 1 and player2[0] == 10):
            secondPlayerFlag = 2
        else:
            secondPlayerFlag = 1

        firstPlayerScore += firstPlayerFlag * player1[i]
        secondPlayerScore += secondPlayerFlag * player2[i]

    print(firstPlayerScore)
    print(secondPlayerScore)
    return 1 if firstPlayerScore > secondPlayerScore else 2 if secondPlayerScore > firstPlayerScore else 0


# player1 = [9,7,10,7]
# player2 = [10, 2, 4, 10]
# player1 = [10, 2, 2, 3]
# player2 = [3, 8, 4, 5]
# print(isWinner(player1, player2))