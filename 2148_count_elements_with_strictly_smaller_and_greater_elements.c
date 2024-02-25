int countElements(int* nums, int numsSize) {
    int count = 0;
    int main_flag, greater_flag, smallest_flag;

    for (int i = 0; i < numsSize; i++) {
        main_flag = 0;
        greater_flag = smallest_flag = 1;

        for (int j = 0; j < numsSize; j++) {
            if (greater_flag && nums[j] > nums[i]) {
                main_flag += 1;
                greater_flag = 0;
            }
            if (smallest_flag && nums[j] < nums[i]) {
                main_flag += 1;
                smallest_flag = 0;
            }
        }

        if (main_flag == 2) count += 1;
    }

    return count;
}