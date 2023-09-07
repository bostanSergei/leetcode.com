from itertools import groupby

def isLongPressedName(name, typed):
    '''
    :param name: имя, которое нужно набрать на клавиатуре
    :param typed: имя, которое набрали на западающей клавиатуре
    :return: bool -->> похоже ли то что собирались набрать на то, что получилось)
    lvl - easy. Чуть подробнее о задаче. Представим, что мы хотим набрать АБВ. В процессе набора может получится так,
    что какой-то из символов (или группа символов) будут набраны несколько раз (больше чем нужно (например АААБВВ)).
    Это нормально - клавиатура то западает. Главное, чтоб символов было не меньше чем нужно. К примеру если ожидаем
    ААБВ, а получаем АБВ, то вернуть нужно будет False, так как символов буквы А в результате меньше чем в ожидаемой
    строке. С этой задачей, я, если честно долго тупил) Сначала хотел вспомнить регулярки и пробежавшись по первой
    строке хотел составить паттерн, который я планировал сравнить с результатом. До регулярок не дошел, так как вспомнил
    про itertools и groupby и решил, что вспомнить этот модуль будет логичнее в решении конкретно этой задачи.
    В общем, получилось не плохо) И задачу решили и по пройденному материалу пробежались)
    '''
    nameGroupList = [[key, list(val)] for key, val in groupby(name)]
    typedGroupList = [[key, list(val)] for key, val in groupby(typed)]
    if len(nameGroupList) != len(typedGroupList):
        return False

    for first, second in zip(nameGroupList, typedGroupList):
        if first[0] != second[0] or len(first[1]) > len(second[1]):
            return False
    return True


# name = "saeed"
# typed = "ssaaedd"
# name = "alex"
# typed = "aaleex"
# print(isLongPressedName(name, typed))