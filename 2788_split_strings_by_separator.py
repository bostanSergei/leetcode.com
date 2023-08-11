def splitWordsBySeparator(words, separator):
    '''
    :param words: список слов/предложений, в которых есть (а может и нет)) разделителя, по которму
    нужно будет разбить строку на отдельные "слова". "Пустоту" не добавляем)
    :param separator: собственно сам разделитель.
    :return: Возвращаем итоговый список.
    '''
    resList = []
    for i in words:
        newList = i.split(separator)
        for j in newList:
            if j:
                resList.append(j)

    return resList


# for test
# words = ["$easy$","$problem$"]
# separator = "$"
# words = ["one.two.three","four.five","six"]
# separator = "."
# words = ["|||"]
# separator = "|"
# print(splitWordsBySeparator(words, separator))