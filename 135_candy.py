def candy(ratings: list) -> int:
    '''
    :param ratings: список чисел. Каждое число - рост очередного ребенка.
    :return: минимальное количество конфет, которые мы можем раздать всем детям при следующем условии:
    если у ребенка есть соседи, но при этом он самого маленького роста, ему достанется одна конфета.
    если рядом с ребенком есть кто-то кто ниже его, то у этого ребенка должно быть как минимум на одну
    конфету больше. lvl - hard. Решать задачу будем за два прохода. Сначала будем сравнивать каждого
    текущего со следующим, а затем каждого текущего с предыдущим, раздавая конфеты в соответствии с условием
    '''
    numCandies = [1] * len(ratings)

    for i in range(len(ratings) - 1):
        if ratings[i] < ratings[i + 1]:
            numCandies[i + 1] = max(1 + numCandies[i], numCandies[i + 1])

    for j in range(len(ratings) - 2, -1, -1):
        if ratings[j + 1] < ratings[j]:
            numCandies[j] = max((1 + numCandies[j + 1], numCandies[j]))

    return sum(numCandies)


ratings = [1, 0, 2]
print(candy(ratings))
