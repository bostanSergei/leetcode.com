def addedInteger(nums1: list, nums2: list) -> int:
    return (sum(nums2) - sum(nums1)) // len(nums1)
