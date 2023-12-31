def minimumCost(cost):
    '''
    :param cost: список чисел - цена конфет в магазине
    :return: вернуть наименьшую сумму, которую потратит покупатель на все конфеты с учетом скидки
    суть скидки: покумаешь две конфеты и третью получаешь в подарок. Стоимость третей конфеты должна быть
    не больше суммы двух других конфет.
    Задача сводится к разделению отсортированного по убыванию массива на чанки по 3, где в итоговой сумме
    принимаеют участие две предыдущие конфеты, а третья не учитывается.
    lvl - easy. Пока писал описание, подумал что и на чанки можно не делить. Просто enumerate введем, где
    каждый третий элемент не будем учитывать)
    '''
    result = 0
    for ind, price in enumerate(sorted(cost, reverse=True), 1):
        if ind % 3 == 0:
            continue
        else:
            result += price

    return result