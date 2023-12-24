def kthSmallestPrimeFraction(arr: list, k: int) -> list:
    fracList = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            fracList.append([arr[i], arr[j], round(arr[i] / arr[j], 10)])

    fracList.sort(key=lambda x: x[2])

    return fracList[k - 1][:2]


arr = [1, 2029, 3209, 3517, 3823, 4933, 8209, 8893, 12763, 12799, 14197, 14387, 18973, 19207, 23747, 24547, 24953, 25247, 25763, 27043]
k = 1
print(kthSmallestPrimeFraction(arr, k))
