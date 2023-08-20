def finalString(s):
    '''
    :param s: строка, которую пытаются напечатать на сломанной клавиатуре
    :return: вернуть, строку, которая получится в результате ввода)
    задача easy lvl, опэтому решение максимально тривиальное. Смысл поломки:
    каждый раз когда нажимают на букву i, то строка переворачивается
    '''
    resultString = ''
    for i in s:
        if i == 'i':
            resultString = resultString[::-1]
        else:
            resultString += i
    return resultString


# s = "string"
# print(finalString(s))