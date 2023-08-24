from collections import Counter


def frequencySort(s):
    '''
    :param s: строка на вход, которую нужно отсортировть. lvl - medium
    :return: правило сортировки: чем выше частота буквы в строке - тем выше "приоритет" символа. Заглавные
    и строчне буквы - разные символы. Несмотря на уровень задачи, решается она достаточно просто. Да, не
    с первого раза (мое решение сортировокой прямо в лоб не прошло на этапе половины тестов), но тем не менее)
    '''
    dictCounter = Counter(s)
    resList = sorted([[key, val] for key, val in dictCounter.items()], key=lambda x: -x[1])
    resString = ''
    for i, j in resList:
        resString += j * i
    return resString


# s = "Aabb"
# print(frequencySort(s))