def flipAndInvertImage(image):
    '''
    :param image: матрица, которую на мнеобхоимо инвертировать и перевернуть каждую строку
    :return: результирующая матрица
    Задача на самом деле достаточно простая. Всемто описания, покажу старт и финиш и все всанет на свои места
    1, 1, 0            1, 0, 0   Я создал функцию, которая возвращает инврт от входящего числа
    1, 0, 1   --->>>   0, 1, 0   и с помощью генератора списков заменил текущую строку из цикла for
    0, 0, 0            1, 1, 1   Далее - срезом перевернул полученный список и добавли в resultList
    '''
    resultList = []
    def changeNumber(num):
        if num == 1:
            return 0
        elif num == 0:
            return 1
    for i in image:
        resultList.append([changeNumber(j) for j in i][::-1])

    return resultList

# for test
# image = [[1,1,0],[1,0,1],[0,0,0]]
# print(flipAndInvertImage(image))