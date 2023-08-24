import random

class Solution:
    '''
    Нееобходимо реализовать класс, в котором будет два метода: инициализатор и метод pick
    Суть метода - возвращать случайный индекс из списка чисел объекта, если число равно target
    Крайне старнная и простая задача, особенно учитывая её уровень на leetcode - medium
    '''
    def __init__(self, nums: list):
        self.newList = []
        self.newList.extend(nums)

    def pick(self, target: int) -> int:
        resList = [i for i in range(len(self.newList)) if self.newList[i] == target]
        return random.choice(resList)