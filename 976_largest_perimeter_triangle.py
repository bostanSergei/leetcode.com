def largestPerimeter(nums):
    '''
    :param nums: список чисел (предполагаемые строны треугольника)
    :return: вернуть максимально возможную сумму сторон треугольника или ноль, если из чисел в списке
    невозможно построить ни один треугольник.
    Итак, задача easy lvl. Для решения возьмем за основу факт, что каждая сторона треугольника
    должна быть меньше суммы двух остальных сторон. Это - правило, на которое мы будем посматривать)
    Отсортируем наш изначальный список по убыванию и начнем бежать по нему циклом.
    Представим, что после сортиовки мы получим что-то типа [15, 15, 13, 8, 2, 2, 1]. Несложно догадаться
    что треугольников типа 15-15-1 или 15-13-2 у нас существовать не может. Это должны быть близкие друг
    к другу числа. Для этого и сортируем. Из нашего списка только мы сможем собрать три треугольника:
    (15, 15, 13) и (15, 13, 8) и (2, 2, 1). Логично, что самым большим треугольником будет первый.
    Поэтому его сумму мы сразу и возвращаем
    '''
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        first, second, third = nums[i], nums[i + 1], nums[i + 2]
        if first < second + third:
            print([first, second, third])
    return 0



# nums = [15, 15, 13, 8, 2, 2, 1]
# print(largestPerimeter(nums))