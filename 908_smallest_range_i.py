def smallestRangeI(nums: list, k: int) -> int:
    '''
    :param nums: список чисел
    :param k: число, которое может принимать участие в формировании нового списка в диапазоне от -k до +k
    :return: вернуть разницу между максимальным и минимальным числом из списка после изменения числа из списка
    на диапазон от -k до +k.
    lvl - easy. Вообще, условие задачи максимально тупое и сделано лишь для того, чтобы запустать того, кто будет её
    решать. К примеру, дается входнйо массив [1, 3, 6] с параметром k равным 3. Нам предлагают к единице прибавить 3,
    к тройке прибавить 1, к шестерке прибавить -2. Все эти три числа (3, 1 и -2) находятся в том самом диапазоне от
    -k до +k. в итоге мы якобы получаем массив [4, 4, 4], в котором разница между макисамльным и минимальным равно нулю.
    Этот ноль мы типа и должны вернуть. Однако по той же самой логике мы можем сформировать массив [3, 3, 3] в котором
    1 + 2 = 3, 3 + 0 = 3 и 6 + (-3) = 3. Короче, ребята, которые писали условие всеми симлами пытались запутать тех, кто
    её будет решать. По факту всё сводится к нахождению макс и мин из списка и сравнением с двойным k, после которого
    можно либо сразу вернуть 0 либо, разницу между макс минус k и минимум плюc k
    '''
    maxNum, minNum = max(nums), min(nums)
    diff = maxNum - minNum
    if 2 * k < diff:
        return (maxNum - k) - (minNum + k)
    else:
        return 0
