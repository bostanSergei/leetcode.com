def compareVersion(version1: str, version2: str) -> int:
    version1, version2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
    p1, p2 = 0, 0
    while p1 < len(version1) and p2 < len(version2):
        if version1[p1] == version2[p2]:
            p1 += 1
            p2 += 1
        elif version1[p1] > version2[p2]:
            return 1
        elif version1[p1] < version2[p2]:
            return -1

    if p1 < len(version1) and sum([version1[p1:]]) == 0:
        return 0
    elif p1 < len(version1) and sum([version1[p1:]]) > 0:
        return 1

    if p2 < len(version2) and sum(version2[p2:]) == 0:
        return 0
    elif p2 < len(version2) and sum(version2[p2:]) > 0:
        return -1

    return 0


# version1 = "1.0"
# version2 = "1.0.0"
# print(compareVersion(version1, version2))
