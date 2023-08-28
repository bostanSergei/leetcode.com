def numWaterBottles(numBottles, numExchange):
    '''
    :param numBottles: стартовое количество полных бутылок с водой
    :param numExchange: количество пустых бутылок, которые мы можем поменять на одну полную бутылку с водой
    :return: сколько бутылок воды мы сможем выпить, если каждый раз будем менять пустые бытулки по обозначенным правилам
    lvl - easy, классическая задача на цикл while. Пьем - меняем, и так до тех пор, пока количества пустых бутылок
    нам не будет хватать для обмена
    '''
    result = numBottles

    while numBottles >= numExchange:
        result += numBottles // numExchange
        numBottles = numBottles // numExchange + numBottles % numExchange

    return result


# numBottles = 15
# numExchange = 4
# print(numWaterBottles(numBottles, numExchange))