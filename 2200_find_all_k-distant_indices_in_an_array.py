def findKDistantIndices(nums, key, k):
    resList = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(i - j) <= k and nums[j] == key:
                resList.append(i)
                break

    return resList


# nums = [3,4,9,1,3,9,5]
# key = 9
# k = 1
# print(findKDistantIndices(nums, key, k))