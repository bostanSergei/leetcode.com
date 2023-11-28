import random


def findKthLargest(nums: list, k: int) -> int:
    '''
    :param nums: список чисел
    :param k: порядковый номер числа, которое нужно вернуть (в отсортированной по убыванию последовательности)
    :return: вернуть число. Выполнить задачу без использования сортировки
    Классическая задача для поиска k-ого числа в неупорядоченной последованиельности. Мы выбираем из списка
    опорный элемент и раскидываем числа по трем разным спискам: числа больше (или меньше в зависимости от условия
    задачи) опорного элмента, те что меньше и те что равны. А далее рекурсивно обращаемся к тому же самому алгоритму
    по массиву, в котором находится k-ый элемент.
    '''
    leftList, middleList, rightList = [], [], []
    randomIndex = random.randint(0, len(nums) - 1)
    for num in nums:
        if num > nums[randomIndex]:
            leftList.append(num)
        elif num == nums[randomIndex]:
            middleList.append(num)
        else:
            rightList.append(num)

    if k <= len(leftList):
        return findKthLargest(leftList, k)

    elif k > len(leftList) + len(middleList):
        return findKthLargest(rightList, k - (len(leftList) + len(middleList)))

    else:
        return middleList[0]


# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(findKthLargest(nums, k))
