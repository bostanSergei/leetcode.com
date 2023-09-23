from datetime import datetime, timedelta

def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    '''
    :param arriveAlice: дата приезда Алисы
    :param leaveAlice: Дата отъезда Алисы
    :param arriveBob: дата прибытия Боба
    :param leaveBob: Дата отъезда Боба
    :return: Сколько дней Боб и Алиса провели вместе?
    '''
    countDays = 0
    arriveAlice = datetime.strptime(arriveAlice + '-1900', '%m-%d-%Y')
    leaveAlice = datetime.strptime(leaveAlice + '-1900', '%m-%d-%Y')
    arriveBob = datetime.strptime(arriveBob + '-1900', '%m-%d-%Y')
    leaveBob = datetime.strptime(leaveBob + '-1900', '%m-%d-%Y')
    delta = timedelta(days=1)
    while arriveAlice <= leaveAlice:
        if arriveBob <= arriveAlice <= leaveBob:
            countDays += 1
        arriveAlice += delta
    return countDays


# arriveAlice = "08-15"
# leaveAlice = "08-18"
# arriveBob = "08-16"
# leaveBob = "08-19"
# print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
