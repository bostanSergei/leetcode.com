def mergeArrays(nums1, nums2):
    '''
    :param nums1: двумерный массив. Каждый элемент - два целых числа. Первое число - порядковый номер. Второе - значение
    :param nums2: такой же двумерный массив, которые необходимо объеденить по следующему правилу:
    если порядковый номер массивов совпадает - добавляем в результирующий массив сам порядковый номер и сумму значений
    если не совпадают - пары без изменений. Массивы уже отсортированы по порядковому номеру
    :return: вернуть результирующий массив
    [1, 3], [2, 4], [4, 6]      собственно логика изложена на этом примере. Первые два элемента имеют одинаковый
    [1, 5], [2, 2], [7, 2]      порядковый номер. Их значения мы сложили. Последние элементы имеют разные порядковые
    ----------------------      номера. Поэтому мы добавили их в результирующий список без изменений
    [1, 8], [2, 6], [4, 6], [7, 2]
    lvl - easy. Руководствуемся логикой двух указателей
    '''
    first, second, resultList= 0, 0, []
    while first < len(nums1) and second < len(nums2):
        if nums1[first][0] == nums2[second][0]:
            resultList.append([nums1[first][0], nums1[first][1] + nums2[second][1]])
            first += 1
            second += 1
        elif nums1[first][0] < nums2[second][0]:
            resultList.append(nums1[first])
            first += 1
        elif nums1[first][0] > nums2[second][0]:
            resultList.append(nums2[second])
            second += 1
    if first < len(nums1):
        for lst in nums1[first:]:
            resultList.append(lst)
    elif second < len(nums2):
        for lst in nums2[second:]:
            resultList.append(lst)

    return resultList


# nums1 = [[2,4],[3,6],[5,5]]
# nums2 = [[1,3],[4,3]]
# nums1 = [[1,2],[2,3],[4,5]]
# nums2 = [[1,4],[3,2],[4,1]]
# print(mergeArrays(nums1, nums2))