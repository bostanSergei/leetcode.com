def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
    lenList = [len(s1), len(s2), len(s3)]
    index = 0
    while index < min(lenList):
        if len(set(f'{s1[index]}{s2[index]}{s3[index]}')) > 1:
            break
        index += 1

    if index == 0:
        return -1
    return sum(lenList) - index * 3


# s1 = "abc"
# s2 = "abb"
# s3 = "ab"
# print(findMinimumOperations(s1, s2, s3))
