int findClosestNumber(int* nums, int numsSize) {
    int result_num = nums[0];
    int curr_num, flag;
    flag = 1;
    for (int i = 0; i < numsSize; i++) {
        curr_num = nums[i];
        if (curr_num < 0) {
            curr_num *= -1;
        }

        if (result_num < 0) {
            flag = -1;
        } else {
            flag = 1;
        }

        if (curr_num < result_num * flag) {
            result_num = nums[i];
        } else if (curr_num == result_num * flag) {
            if (nums[i] > result_num) {
                result_num = nums[i];
            }
        }
    }

    return result_num;
}