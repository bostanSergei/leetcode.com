def minCostClimbingStairs(cost):
    '''
    :param cost: список чисел, по которым мы можем перемещаться либо поэлементно, либо через 1
    :return: задача - вернуть наименьшую сумму, которую мы можем собрать, пройдя по списку от начала
    до конца. lvl - easy. Несмотря на уровень сложности задачи с рекурсией мне даются жутко сложно =(
    до сих пор не понимаю эту тему. Выполнил задачу каким-то чудом, не понимая до конца как это работает.
    Пытаюсь вернуться на тему рекурсий уже в который раз, но каждый раз снова застреваю
    '''
    cache = {}

    def recursionFunc(num):
        if num < 2:
            return cost[num]
        if num not in cache:
            cache[num] = cost[num] + min(recursionFunc(num - 1), recursionFunc(num - 2))
        return cache[num]

    num = len(cost)
    return min(recursionFunc(num - 1), recursionFunc(num - 2))


# cost = [1, 2, 2, 0]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# print(minCostClimbingStairs(cost))
