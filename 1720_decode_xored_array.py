def decode(encoded, first):
    '''
    :param encoded: список, который нужно "декодировать"
    :param first: первый элемент финального списка
    :return: вернуть новый список. Список получаем "исключающим ИЛИ" (a XOR b), где а - последний элемент
    результирующего списка, b - очередной элемент списка encoded
    lvl - easy. Я на самом деле до сих пор не самым лучшим образом понимаю битовые операции, однако эта
    задача по скорости лучше чем 99,93% прошлых решений
    '''
    resList = [first]
    for i in range(len(encoded)):
        resList.append(resList[i] ^ encoded[i])

    return resList


# encoded = [6, 2, 7, 3]
# first = 4
# print(decode(encoded, first))
