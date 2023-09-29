def alternatingSubarray(nums) -> int:
    '''
    :param nums: дан массив целых чисел. Нам нужно в этом массиве выделить подмассивы, которые соответствуют
    следующему условию: s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1 и так далее.
    :return: Если такие массивы существуют, нужно вернуть длину самого большого подмассива, иначе -1
    '''
    resList = []
    for i in range(len(nums) - 1):
        currLst = nums[i:]
        for j in range(1, len(currLst)):
            if j % 2 == 1:
                if currLst[j] - currLst[j - 1] == 1:
                    resList.append(len(currLst[:j + 1]))
                else:
                    break
            else:
                if currLst[j] - currLst[j - 1] == -1:
                    resList.append(len(currLst[:j + 1]))
                else:
                    break

    return max(resList) if len(resList) > 0 else -1


# nums = [2, 3, 4, 3, 4]
# nums = [4, 5, 6]
# print(alternatingSubarray(nums))
