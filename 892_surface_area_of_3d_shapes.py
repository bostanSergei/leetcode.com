def surfaceArea(grid):
    '''
    :param grid: дана матрица, которая символизирует поле размерами (n * n) в котором каждое значение символизирует
    количество кубиков размером 1 на 1 на 1, стоящих друг на друге
    :return: нам нужно вернуть площадь всех видимых граней нашей "объемной" фигуры
    эту задачу я откравывал уже неоднократно, однако да текущего момента мне она казалась какой-то сложной и я даже
    не пробовал её решить. Что изменилось сейчас - не понятно, но это точно успех =))) lvl на leetcode - easy
    Итак, смысл. Представим список (пока одномерный): [1, 2, 0, 3]. каждый элемент это куб с размерами 1 x 1 x 1
    То есть у нас на первом месте стоит 1 кубик, рядом с ним два кубика один на другом, потом пустое простанство и 3 кубика
    Представим эту объемную фигуру и посчитаем её площадь. Во первых, поскольку массив одномерный, мы можем посчитать
    площадь "лицевой части" и умножить её на 2 (ничего не мешает ни сзади ни спереди). (1 + 2 + 0 + 3) * 2 = 12
    Во вторых у нас есть вид сверху и снизу. (1 + 1 + 0 + 1) * 2 = 6. Остается самое "сложное". Вид слева и справа.
    Для первого кубика открытой площадью является только площадь слева - она равна единице. Справа вплотную стоят
    два других кубика, поэтому "эту грань мы не видим". Идем дальше. Два других кубика (друг на друге стоят).
    Слева - 1 (верхний, так как нижний закрывает первый кубик), справа - 2 (так как следующий элемент - 0 - пустое место).
    Остается последний элемент (три куба друг на друге). Слева - 3 (так как до этого было пустое место) и справа - 3
    (так как дельше ничего нет). Сложив полученные цифры вместе мы получим нашу заветную площадь.
    Единственное, в задаче массив не одномерный, а двумерный, но логика расчетов - плюс минут та же.
    Надеюсь мое объяснение кому-то помогло)
    '''
    result = 0
    lst = [i for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 0:
                currientArea = 2
                if i - 1 not in lst:
                    currientArea += grid[i][j]
                else:
                    area = grid[i][j] - grid[i - 1][j]
                    currientArea += area if area > 0 else 0
                if i + 1 not in lst:
                    currientArea += grid[i][j]
                else:
                    area = grid[i][j] - grid[i + 1][j]
                    currientArea += area if area > 0 else 0
                if j - 1 not in lst:
                    currientArea += grid[i][j]
                else:
                    area = grid[i][j] - grid[i][j - 1]
                    currientArea += area if area > 0 else 0
                if j + 1 not in lst:
                    currientArea += grid[i][j]
                else:
                    area = grid[i][j] - grid[i][j + 1]
                    currientArea += area if area > 0 else 0
                result += currientArea
    return result


# grid = [[1,1,1],[1,0,1],[1,1,1]]
# print(surfaceArea(grid))
