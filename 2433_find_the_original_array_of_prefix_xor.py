def findArray(pref):
    '''
    задачи с побитовыми операциями мне од сих пор даются очень сложно. Методом проб и ошибок я как-то решил эту
    задачу. Я абсолютно точно понимаю алгоритм своиз действий, но когда в голове не укладываются логика работы
    в двоичном формате - все превращается в кашу. Объяснить суть задачи не смогу. Сделать - сделал. Без подсказок
    и других решений - исключительно на работе с тестовыми данными. Понял - алгоритм, поработал с принтом - написал.
    lvl - medium, и обычно я в медиум по непонятным мне темам не лезу, но тут, звезды сошлись)
    upd: пошел в решения и понял, что я чет очень сильно намудрил. Там решения в одну строку в цикле. А я зачем-то
    перекладываю значения из одного корыта в другое. Грустно стало =(
    '''
    startNum = pref[0]
    resList = [pref[0]] * len(pref)
    for i in range(1, len(resList)):
        currient = startNum ^ pref[i]
        resList[i] = currient
        pref[i] = currient
        currient = startNum
        startNum = currient ^ pref[i]

    return resList


# pref = [5, 2, 0, 3, 1]
# print(findArray(pref))
# [5, 7, 2, 3, 2]

