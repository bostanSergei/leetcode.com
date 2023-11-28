def constructProductMatrix(grid: list) -> list:
    '''
    :param grid: матрица
    :return: вернуть новую матрицу
    задачка конечно жесть) попила кровушки) lvl - medium. Суть задачи - создать новую матрицу с такой же размерностью
    как и стартовая, но каждый элемент матрицы - это произведение всех остальных элементов матрицы кроме того, на который
    мы смотрим в настоящий момент времени по модулю на число 12345. Расписывать решение думаю нет особо смысла:
    код максимально понятен. Идея первого цикла и идея пары дополнительных условий связана с вопросом о необходимости
    или НЕ необходимости лишних вычислений, которые забирают на себя кучу времени при этом никак не влияя на исход.
    '''
    row, col, mod = len(grid), len(grid[0]), 1
    matrix = [[0] * col for i in range(row)]
    indexesList, zeroCount = [], 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] % 12345 == 0:
                indexesList.append([i, j])
                zeroCount += 1

    if zeroCount >= 2:
        return matrix

    for i in range(row):
        for j in range(col):
            mod *= grid[i][j]

    if zeroCount == 1:
        matrix[indexesList[0][0]][indexesList[0][1]] = (mod // grid[indexesList[0][0]][indexesList[0][1]]) % 12345
        return matrix

    for i in range(row):
        for j in range(col):
            matrix[i][j] = (mod // grid[i][j]) % 12345

    # print(*matrix, sep='\n')
    return matrix


grid = [[435359696],[794672023],[847201075],[233627034],[602266227],[530987019],[807603630],[568863829],[525440873],[431916276],[111724495],[820059934],[590293791],[316791645],[856216515],[799447875],[511599706],[332868914],[626858747],[103810960],[184650614],[188764893],[216452847],[662697310],[223975305],[403174470],[543813895],[80436555],[427442614],[667816145],[140407927],[520403986],[953514667],[124289499],[505669503],[325293763],[413268604],[697864924],[833764613],[688928026],[159043889],[492671076],[706013067],[151203319],[888941049],[65272947],[580659420],[284485179],[149859181],[898169716],[595933247],[658730545],[357261663],[750495856],[937356149],[554381227],[193814809],[598034540],[50359047],[492060899],[618452011],[257170366],[255066579],[754454335],[863731515],[956053597],[390602538],[699360118],[705433713],[918418120],[676663678],[131773817],[785063839],[273135204],[770459063],[864886873],[789003106],[58760659],[608615959],[780519767],[616188616],[370777672],[663700465],[542219871],[893205166],[209537591],[377889710],[610267005],[336826777],[518463498],[926330851],[507577727],[247469046],[547975865],[643658786],[310031477],[273931554],[728736564],[165403561],[902964931],[428353592],[216699766],[891042023],[11810380],[923310963]]
# grid = [[12345], [2], [1]]
print(constructProductMatrix(grid))
