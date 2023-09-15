def calculateTax(brackets, income):
    '''
    :param brackets: дан двумерный массив в котором находятся списки, состоящие из двух целых чисел: доход и налог в процентах
    :param income: ограничение на доход
    :return: вернуть налог, который мы должны заплатить исходя из входных параметров
    lvl - easy - условие запутанное донельзя)
    Суть: [[3, 50], [7, 10], [12, 25]], income = 10.
    На первом шаге мы возьмем 3 доллара и заберем налог на в 50 процентов (1.50)
    На втором мы должны от 7 долларов отнять 3 (с предыдущего шага) и с 4 долларов снять налог 10 процентов, т.е. 0.4 доллара
    На третьем мы с 12 долларов отнимаем 7 (предудыщий шаг) -> получаем 5 долларов, но (3 + 4 = 7)  а (7 + 5 = 12), что больше
    чем income в 10 долларов. Соответственно послений налог мы должны снять не с 5 долларов а с 3-ёх, которых не хватает до
    десятки. С 3 долларов 25 процентов это 0.75
    Остается только сложить 1.5 + 0.4 + 0.75 = 2.65 и именно это число мы и должны вернуть.
    '''
    tax, count = 0, 0
    for i in range(len(brackets)):
        if i == 0:
            if brackets[i][0] >= income:
                tax += income * (brackets[i][1] / 100)
                return tax
            else:
                tax += brackets[i][0] * (brackets[i][1] / 100)
                count += brackets[i][0]
        else:
            if (brackets[i][0] - brackets[i - 1][0]) + count >= income:
                tax += (income - count) * (brackets[i][1] / 100)
                return tax
            else:
                tax += (brackets[i][0] - brackets[i - 1][0]) * (brackets[i][1] / 100)
                count += (brackets[i][0] - brackets[i - 1][0])
    return tax


brackets = [[1, 0], [4, 25], [5, 50]]
income = 2
print(calculateTax(brackets, income))
