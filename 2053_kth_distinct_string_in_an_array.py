from collections import Counter

def kthDistinct(arr, k):
    '''
    :param arr: список слов, букв, символов
    :param k: порядковый номер уникального символа (набора символов) из списка arr, окторый следует вернуть
    :return: сам элемент списка arr. Пример: [день, вода, утро, вода, ночь, утро, солнце], k = 3.
    У нас есть три уникальных слова. День, ночь, солнце. "к" при этом тоже равна трем. То етсь вернем солнце.
    Именно солнце третье по счету. Если бы "к" была равна 2, то вернули бы ночь, а если бы 4 - то пустую строку
    lvl - easy, good time
    '''
    newDict, count = Counter(arr), 0
    for i in arr:
        if newDict[i] == 1:
            count += 1
            if count == k:
                return i
    return ''


# arr = ["aaa","aa","a"]
# k = 1
# print(kthDistinct(arr, k))
