def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    '''
    :param length, width, height, mass: три размера коробки и его масса
    :return: вернуть какой является коробка. Либо тяжелой, либо громоздкой, либо И тяжелой И громоздкой
    либо ни тем ни тем. В общем, супер простая задача - простые математические операции и группа ифов
    в правильном порядке. lvl - easy
    '''
    firstFlag, secondFlag = False, False
    if max([length, width, height]) >= 10 ** 4 or length * width * height >= 10 ** 9:
        firstFlag = True
    if mass >= 100:
        secondFlag = True
    if all([firstFlag, secondFlag]):
        return 'Both'
    elif firstFlag:
        return 'Bulky'
    elif secondFlag:
        return 'Heavy'
    else:
        return 'Neither'


length, width, height, mass = 1000, 35, 700, 300
print(categorizeBox(length, width, height, mass))
