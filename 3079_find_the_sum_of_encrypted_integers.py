def sumOfEncryptedInt(nums: list) -> int:
    res = 0
    for num in nums:
        max_num = max(str(num))
        res += int(max_num * len(str(num)))

    return res
