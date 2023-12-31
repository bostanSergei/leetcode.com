def minOperations(logs):
    '''
    :param logs: список логов, в котором записаны перемещения пользователя по папкам. В самом начале мы находимся
    в корневом каталоге (выше нет ничего). В процессе перемещения по списку логов мы можем или переместиться в
    родительскую папку, или остаться в текущей папке или перейти в дочернюю папку. Когда список логов закончится:
    :return: вернуть количество шагов до main-папки (стартовой главной)
    lvl - easy. Решаем простым перебором списка и уменьшением или увеличением стартового значения.
    '''
    step = 0
    for i in logs:
        if i == '../' and step > 0:
            step -= 1
        elif i == '../' and step == 0:
            continue
        elif i == './':
            continue
        else:
            step += 1
    return step


# logs = ["d1/","d2/","./","d3/","../","d31/"]
# logs = ["d1/","d2/","../","d21/","./"]
# logs = ["d1/","../","../","../"]
# print(minOperations(logs))