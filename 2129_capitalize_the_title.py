def capitalizeTitle(title):
    '''
    :param title: строка, которую нужно вернуть, изменив регистр по правилам задачи
    :return: если длина слова больше двух символов - первая буква заглавная, остальные
    строчные. Если слово меньше трех символов - все символы строчные
    '''
    return ' '.join([i.title() if len(i) > 2 else i.lower() for i in title.split()])


# title = "First leTTeR of EACH Word"
# print(capitalizeTitle(title))