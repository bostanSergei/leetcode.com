def convert(s: str, numRows: int) -> str:
    '''
    :param s: дана строка, которую нужно "представить" в "особенном" виде. А после этого "отформатировать" по полученному
    представлению.
    :param numRows: количество "столбцов"
    :return: полученная строка.
    Уффф. У задачи крайне странное условие. Это одна из тех задач, которую трудно сформулировать. Автор накрутил такого,
    что словами не описать. Проще показать.
    Дана строка: PAYPALISHIRING и количество строк равным 4. Требуется посимвольно считывать символы строки и записывать
    их тем самым "зиг-заг" способом:
    P   A   H   N       Перый шаг сверху вниз, пока не дойдем по ограничения по numRows
    A P L S I I G       Следующий шаг - по диагонали вверх. И так до тех пор, пока слово не закончится
    Y   I   R           После этого нужно прочитать полученный набор символов слева направо сверху вниз
    То есть получить строку PAHNAPLSIIGYIR (PAHN + APLSIIG + YIR)
    Задача medium lvl с 13к дизов (что в целом не удивительно). Пытался подойти к ней пару месяцев назад, но то ли
    было лень, толи не хотелось думать. В итоге решил поступить необычным образом: в целом все это очень похоже на
    матрицу. Так почему бы эту матрицу нам и не изобразить. Сначала инициализировать её нулями, а потом заполнять
    по имеющемуся алгоритму до тех пор, пока буквы не кончатся. После этого останется просто считать матрицу
    "по человечески", пропуская нули и забирая только то что нам нужно в финальную строку.
    Не сказать, что задача заняла много времени, но признаться честно, она очень странная. Моё время выполнения
    страдает, но в решения не полез и исправлять не буду. Пускай то что работает, продолжает работать)
    '''
    if numRows == 1:
        return s

    index, direction, wordLen = 0, 'down', len(s)
    matrix = [['0' for i in range(wordLen // 2 + 1)] for j in range(numRows)]

    rowIndex, colIndex = -2, 1
    while index < wordLen:
        if direction == 'down':
            rowIndex += 2
            colIndex -= 1
            while rowIndex < numRows:
                matrix[rowIndex][colIndex] = s[index]
                rowIndex += 1
                index += 1

                if index == wordLen:
                    break

            direction = 'diagonal'

        elif direction == 'diagonal':
            rowIndex -= 2
            colIndex += 1
            while rowIndex >= 0:
                matrix[rowIndex][colIndex] = s[index]
                rowIndex -= 1
                colIndex += 1
                index += 1

                if index == wordLen:
                    break

            direction = 'down'

    resultString = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isalpha() or matrix[i][j] in '.,':
                resultString += matrix[i][j]

    # print(*matrix, sep='\n')
    return resultString


# s = "PAYPALISHIRING"
# numRows = 3
# print(convert(s, numRows))
