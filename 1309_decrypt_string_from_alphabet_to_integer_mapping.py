def freqAlphabets(s):
    '''
    :param s: строка, которую нужно декодировать по определенным правилам (указаны в словаре))
    :return: вернуть получившуюся строку.
    '''
    newDict = {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r',
               '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z',
               '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
    result = ''
    while len(s) > 0:
        for key, val in newDict.items():
            if s.startswith(key):
                result += val
                s = s.replace(key, '', 1)
                break
    return result


# s = '10#11#12'
# print(freqAlphabets(s))