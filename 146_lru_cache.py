class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.curr = 0
        self.l = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            param = self.cache[key]
            if (param[0] - self.curr) <= self.l:
                return param[1]
            return -1

    def put(self, key: int, value: int) -> None:
        self.curr += 1
        self.cache[key] = (self.curr, value)


#
# ["LRUCache", "put",   "put", "get", "put",   "get", "put", "get", "get", "get"]
# [[2],         [1, 1], [2, 2], [1],   [3, 3], [2],   [4, 4], [1],   [3],   [4]]
# Output
# [null,        null,    null,   1,     null,  -1,    null,   -1,     3,     4]

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
# obj.put(key,value)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)

print(obj.get(1))
print(obj.get(2))
