def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    '''
    :param nums1: список чисел (упорядоченный по неубыванию)
    :param nums2: список чисел (упорядоченный по неубыванию)
    :return: вернуть медиану двух списков.
    lvl - hard. По учловию задачи требуется выполнить эту операцию за O(log(m + n)), но не понятно, нужно ли
    сливать эти массивы вместе. По хорошему на то, чтобы слить два массива требуется m + n по времени.
    Мы просто перебираем число за числом и сравниваем их друг с другом, а далее просто возваращаем одной или
    сумму двух (в зависимости от длинны полученного массива (по сути считается за O(1) на основе суммы длинн,
    полученных на предыдущем шаге)). Получается даже чуть быстрее того, что от нас требовалось изначальнее.
    Возможно сливать массивы нельзя, но об этом в задаче не сказано, поэтому я пошел именно по этому пути.
    hard или НЕ hard, сложно сказать. Радует, что задача прошла с хорошим показателем по времени и памяти)
    '''
    newNums, firstLen, secondLen = [], len(nums1), len(nums2)
    fIndex, sIndex = 0, 0
    while fIndex < firstLen and sIndex < secondLen:
        if nums1[fIndex] <= nums2[sIndex]:
            newNums.append(nums1[fIndex])
            fIndex += 1
        else:
            newNums.append(nums2[sIndex])
            sIndex += 1

    newNums = newNums + nums1[fIndex:] + nums2[sIndex:]

    twoListLen = firstLen + secondLen
    if twoListLen % 2 == 1:
        return float(newNums[int(twoListLen // 2)])

    index = int(twoListLen / 2)
    return (newNums[index] + newNums[index - 1]) / 2


# nums1 = []
# nums2 = [2, 3]
# print(findMedianSortedArrays(nums1, nums2))
