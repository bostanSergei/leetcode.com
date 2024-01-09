import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n, self.lastIndex = m, n, m * n
        self.indexes = {}
        # self.matrix = [(i, j) for i in range(m) for j in range(n)]

    def flip(self) -> list:
        index = random.choice(range(self.lastIndex))
        self.lastIndex -= 1
        x = self.indexes.get(index, index)
        self.indexes[index] = self.indexes.get(self.lastIndex, self.lastIndex)
        return divmod(x, self.n)
        # index = random.choice(range(self.lastIndex + 1))
        # self.matrix[index], self.matrix[self.lastIndex] = self.matrix[self.lastIndex], self.matrix[index]
        # self.lastIndex -= 1
        # return list(self.matrix[self.lastIndex + 1])

    def reset(self) -> None:
        self.indexes.clear()
        self.lastIndex = self.m * self.n


