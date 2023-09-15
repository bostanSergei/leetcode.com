def sortEvenOdd(nums):
    '''
    :param nums: список чисел
    :return: вернуть новый список, который будет сформирован по следующим правилам:
    все числа, которые стоят на четных индексах нужно отсортировать в порядке возрастания
    числа, которые стоят на НЕчетных индексах - в порядке убывания
    lvl - easy. В целом - классическое решение, написанное ниже - попадает по статистике в одной
    из лучших решений по скорости выполнения - лучше чем 90% предыдущих решений. Поэтому, изобретать
    велосипед не будем и остановимся на нем) Хотя, можно было поиграть с zip_longest из itertools
    '''
    evenNums, oddNums = [], []
    for i in range(len(nums)):
        if i % 2 == 0:
            evenNums.append(nums[i])
        else:
            oddNums.append(nums[i])

    evenNums.sort()
    oddNums.sort(reverse=True)

    resultList = []

    for i in range(min(len(evenNums), len(oddNums))):
        resultList.append(evenNums[i])
        resultList.append(oddNums[i])

    if len(evenNums) > len(oddNums):
        resultList.append(evenNums[-1])
    if len(evenNums) < len(oddNums):
        resultList.append(oddNums[-1])

    return resultList


# nums = [4, 1, 2, 3]
# print(sortEvenOdd(nums))