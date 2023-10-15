def countHillValley(nums: list) -> int:
    '''
    :param nums: список целых чисел. Каждое число символзирует либо гору, либо равнину, либо ничего)
    :return: вернуть количество гор и равнин. Горой считается ситуация в которой число слева и число справа
    от рассматриваемого - меньше самого числа. Равниной: число слева и число справа - больше.
    Крайнее левое и крайнее правое - не рассматриваются. В ситуации [3, 1, 1, 1, 1, 1, 5] - одна равнина.
    Как итог, для начала избавимся от дублей, а уже после будем производить расчеты обычным циклом по списку
    без дублей) lvl - easy
    '''
    result = 0
    newNumsList = [nums[0]]
    for i in nums[1:]:
        if newNumsList[-1] != i:
            newNumsList.append(i)

    for i in range(1, len(newNumsList) - 1):
        if newNumsList[i] > newNumsList[i + 1] and newNumsList[i] > newNumsList[i - 1]:
            result += 1
        elif newNumsList[i] < newNumsList[i + 1] and newNumsList[i] < newNumsList[i - 1]:
            result += 1

    return result


# nums = [2, 4, 1, 1, 6, 5]
# nums = [6, 6, 5, 5, 4, 1]
# print(countHillValley(nums))
