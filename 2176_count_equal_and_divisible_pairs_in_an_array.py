def countPairs(nums, k):
    '''Имеем список чисел. Задача найти такие пары, которые будут равны,
    но при этом идекс i будет меньше индекса j и произведение индексов
    будет делиться на k без остатка. Пробежимся циклом и составим пары,
    а далее будем фильтровать по заданному условию'''
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                if (i * j) % k == 0:
                    result += 1
    return result



# for test
# nums = [3,1,2,2,2,1,3]
# k = 2
# print(countPairs(nums, k))
