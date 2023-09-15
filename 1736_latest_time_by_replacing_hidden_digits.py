def maximumTime(time):
    '''
    :param time: дана страка (время в формате 23:59). На месте любой цифры может стоять знак вопроса
    :return: заменить знако вопроса так, чтоб часы показывали максимально возможное время
    lvl - easy. Хотел не наручивать с условиями, но чет получилось само собой))
    '''
    if time[0] == '?' and time[1] == '?':
        time = time.replace('??', '23', 1)
    def goodNum(index):
        maxTimeNumber = ['2', '4', ':', '5', '9']
        if index > 2:
            return maxTimeNumber[index]
        if index == 0:
            if time[1] > '3':
                return '1'
            else:
                return '2'
        elif index == 1:
            if time[0] == '2':
                return '3'
            else:
                return '9'

    timeList = [goodNum(i) if time[i] == '?' else time[i] for i in range(len(time))]
    return ''.join(timeList)


# time = "1?:22"
# print(maximumTime(time))