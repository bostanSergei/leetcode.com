def accountBalanceAfterPurchase(purchaseAmount):
    '''
    :param purchaseAmount: сумма покупки, которая должна округлиться до 10ти
    :return: вернуть количество денег после покупки, при условии, что изначально денег - 100
    задача чет прям совсем easy-easy. единственное что нужно - входящий параметр округлить до 10ти с
    условием что все что выше 5 - окргуляется в большую сторону
    '''
    startMoney = 100

    num = purchaseAmount % 10
    if num < 5:
        purchaseAmount -= num
    else:
        purchaseAmount += 10 - num
    return startMoney - purchaseAmount
