import json


class FreqStack:
    def __init__(self):
        self.count_dict = {}
        self.dct = {}
        self.max_count = 0

    def push(self, val: int) -> None:
        if val not in self.dct:
            self.dct[val] = 0

        self.dct[val] += 1

        self.max_count = max(self.max_count, self.dct[val])

        if self.dct[val] not in self.count_dict:
            self.count_dict[self.dct[val]] = []

        self.count_dict[self.dct[val]].append(val)

    def pop(self) -> int:
        elem = self.count_dict[self.max_count].pop()
        if len(self.count_dict[self.max_count]) == 0:
            del self.count_dict[self.max_count]
            self.dct[elem] -= 1

            while self.max_count not in self.count_dict and self.max_count > 0:
                self.max_count -= 1

            if self.dct[elem] == 0:
                del self.dct[elem]

        return elem


# with open('test.json', 'r') as file:
#     data = json.load(file)
#
# obj = FreqStack()
#
# for i in data:
#     if len(i) == 0:
#         # try:
#         print(obj.pop())
#         # except:
#         #     print(obj.count_dict)
#         #     print()
#         #     print(obj.dct)
#         #     break
#     else:
#         obj.push(i[0])
