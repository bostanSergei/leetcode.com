def reformatNumber(number):
    '''
    :param number: набор цифр, символов (возможно букв (все тестовые данные не видел)
    :return: вернуть что-то похожее на телефонный номер по определенным правилам (может быть ситуация, когда номер
    будет состоять из двух чисел - попал на этом тестовом с первым решением)
    Итак. В целом правила обозначены в решении. Нверное особого смысла дублировать их тут не имеет большого смысла.
    lvl - easy
    '''
    telList = [i for i in number if i.isdigit()]
    resultString = ''
    while len(telList) > 0:
        if len(telList) > 4:
            for i in range(3):
                resultString += telList.pop(0)
            resultString += '-'
        elif len(telList) == 4:
            resultString += f'{telList[0]}{telList[1]}-{telList[2]}{telList[3]}'
            break
        elif len(telList) == 3 or len(telList) == 2:
            resultString += ''.join(telList)
            break
    return resultString


# number = "1-23-45 6"
# number = "123 4-5678"
# number = "123 4-567"
# print(reformatNumber(number))