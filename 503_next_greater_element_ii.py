def nextGreaterElements(nums):
    '''
    lvl - medium
    :param nums: список чисел
    :return: вернуть новый список по следующему правилу: правило немного запутано, но вот к чему я пришел:
    по сути, если текущее число (в стартовом списке )является максимальным (самым большим), то на его месте
    должна появится минус единица (-1). Если же нет, то мы должны сформировать новый список (цикличный), в
    котором будем искать первое попавшееся число, которое будет больше, чем наше текущее. Условно:
    есть список [3, 6, 1, 9, 7]. Для тройки -> шестерка, для шестерки -> девятка, для единицы -> девятка,
    для девятки -> -1, для семерки -> девятка. То есть в случае с семеркой мы будем рассматривать список
    [3, 6, 1, 9] и искать первое число, которое будет больше семерки. В итоге, финальный список должен иметь
    вид: [6, 9, 9, -1, 9]. В целом, думаю, схема плюс минус понятна. Это было не очень очевидно по тестовым
    данным, которые подаются на вход, но на отладке всё встало на свои места.
    '''
    resultList = []
    maxNumber = max(nums)
    for i in range(len(nums)):
        if maxNumber == nums[i]:
            resultList.append(-1)
        else:
            for j in nums[i:] + nums[:i]:
                if j > nums[i]:
                    resultList.append(j)
                    break
    return resultList


# nums = [5,4,3,2,1]
# nums = [1,2,3,4,3]
# print(nextGreaterElements(nums))