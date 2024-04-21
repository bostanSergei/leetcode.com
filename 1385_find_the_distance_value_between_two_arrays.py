def findTheDistanceValue(arr1: list, arr2: list, d: int) -> int:
    result = 0
    for i in arr1:
        count = 0
        for j in arr2:
            if (x := abs(i - j)) <= d:
                count += 1
        if count == 0:
            result += 1

    return result


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
# arr1 = [1,4,2,3]
# arr2 = [-4,-3,6,10,20,30]
# d = 3
print(findTheDistanceValue(arr1, arr2, d))
