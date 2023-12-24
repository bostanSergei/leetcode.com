def findIntersectionValues(nums1: list, nums2: list) -> list:
    '''
    :param nums1: список чисел
    :param nums2: список чисел
    :return: вернуть список из двух элементов, где первым будет количество чисел из первого списка, которые хоть
    раз встречаются во втором списке. Для второго - аналогично, но уже для чисел из второго в первом. lvl - easy.
    '''
    resultList = [0, 0]
    for i in nums1:
        if i in nums2:
            resultList[0] += 1

    for j in nums2:
        if j in nums1:
            resultList[1] += 1

    return resultList


nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(findIntersectionValues(nums1, nums2))
