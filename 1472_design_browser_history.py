class BrowserHistory:
    # '''Требовалось реализовать класс, представляющий некую историю браузера с указанными митодами. lvl- medium'''

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        if self.pointer < len(self.history) - 1:
            self.history = self.history[:self.pointer + 1]
        self.history.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        if self.pointer - steps < 0:
            self.pointer = 0
        else:
            self.pointer -= steps
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        if self.pointer + steps > len(self.history) - 1:
            self.pointer = len(self.history) - 1
        else:
            self.pointer += steps
        return self.history[self.pointer]

# a = BrowserHistory('leetcode.com')
# a.visit('google.com')
# a.visit('facebook.com')
# a.visit('youtube.com')
# print(a.history)
# print(a.pointer)
# print(a.back(1))
# print(a.back(1))
# print(a.forward(1))
# print(a.pointer)
# a.visit('linkedin.com')
# print(a.history)
# print(a.pointer)
#
# # ["BrowserHistory","  visit",      "visit",        "visit",       "back","back","forward","visit",      " forward","back","back"]
# # [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],   [1],   [1],    ["linkedin.com"],[2],     [2],    [7]]
