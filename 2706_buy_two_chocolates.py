def buyChoco(prices, money):
    '''
    :param prices: список цен на шололад. Задача - купить две шоколадки, не влезая в долги))
    :param money: наш банк, на который будем покупать шлоколад. Не можем уходить в минус
    :return: остаток банка после покупки шоколада. Если не можем купить, вернуть стартовое значение
    '''
    prices.sort()
    bank = money - sum(prices[:2])
    return bank if bank >= 0 else money


# for test
# prices = [3, 2, 3]
# money = 3
# print(buyChoco(prices, money))