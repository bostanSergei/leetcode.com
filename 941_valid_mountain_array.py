def validMountainArray(arr: list) -> bool:
    '''
    :param arr: список чисел (предположительно представляет из себя красивую "гору") =)
    :return: нужно ответить на вопрос: так ли это. Красивой горой считается та, у которой вершина находится где-то
    между первым и последним элементом и каждый следующий элемент справа или слева от вершины будет строго
    меньше чем предыдущий. lvl - easy.
    '''
    maxNumberIndex = arr.index(max(arr))
    if maxNumberIndex == 0 or maxNumberIndex == len(arr) - 1:
        return False
    for i in range(1, maxNumberIndex + 1):
        if arr[i] <= arr[i - 1]:
            return False

    for j in range(maxNumberIndex + 1, len(arr)):
        if arr[j] >= arr[j - 1]:
            return False

    return True


# arr = [3, 5, 5]
# print(validMountainArray(arr))
