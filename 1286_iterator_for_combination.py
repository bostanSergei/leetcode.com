from itertools import combinations

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.element = [''.join(i) for i in combinations(characters, r=combinationLength)]
        self.index = -1

    def next(self) -> str:
        if self.index + 1 < len(self.element):
            self.index += 1
            return self.element[self.index]

    def hasNext(self) -> bool:
        if self.index + 1 < len(self.element):
            return True
        return False

# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]
a = CombinationIterator('abc', 2)
print(a.next())
print(a.hasNext())
print(a.next())
print(a.hasNext())
print(a.next())
print(a.hasNext())
# print(a.next())