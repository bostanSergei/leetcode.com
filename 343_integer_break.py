def integerBreak(n):
    '''
    lvl - medium (Удивительно, но это работает, причем с результатом на 97% лучше других решений)))
    :param n: целое число в диапазоне от 1 до 56
    :return: вернуть максимально возможное произведение чисел, сумма которых равна N
    К идее решения ниже пришел, руководствуясь вот какими мыслями: во первых произведение должны быть
    составлено из чисел первой "пятерки". То есть не имеет никакого смысла собирать суммы из чисел
    больше пяти (в последствии переиграл на четверку). То есть при входящем n=15 надо смотреть на
    произведения троек, чем на, скажем 10 * 5, так как 3 ** 5 будет уж точно больше чем 10 * 5.
    Во вторых, если в списке чисел присутствует единица, то от нее нужно избавиться, увеличивая любое
    соседнее число (ну тут логично - умножая на единицу - произведение не изменится). Отталкиваясь
    от этих размышлений, получилось накидать решение, которые мы видим ниже. К удивлению, решение
    пролетело с первого раза с достойным результатом, поэтому пересобрать то, что итак работает, считаю
    безперспективным. К тому же, это просто задача на leetcode)
    '''
    resList = []
    for i in range(4, 0, -1):
        currientList = []
        newN = n
        flag = True
        while flag:
            currientNum = newN // i
            if currientNum > 0:
                currientList.extend([i] * currientNum)
                newN %= i
            if sum(currientList) == n:
                result = 1
                if len(currientList) == 1:
                    currientList.append(0)
                if 1 in currientList and len(currientList) > 2:
                    del currientList[currientList.index(1)]
                    currientList[0] += 1
                for j in currientList:
                    result *= j
                resList.append(result)
                flag = False
            i -= 1

    return max(resList)

#
# n = 2
# print(integerBreak(n))