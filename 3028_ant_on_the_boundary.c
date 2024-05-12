int returnToBoundaryCount(int* nums, int numsSize) {
    int num = 0;
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        num += nums[i];
        if (num == 0) count += 1;
    }
    return count;
}