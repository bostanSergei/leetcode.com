class MinStack:
    def __init__(self):
        self.lst = []
        self.len_list = 0

    def push(self, val: int) -> None:
        self.lst.append(val)
        self.len_list += 1

    def pop(self) -> None:
        if self.len_list > 0:
            self.lst.pop()
            self.len_list -= 1

    def top(self) -> int:
        if self.len_list > 0:
            return self.lst[-1]

    def getMin(self) -> int:
        return min(self.lst)
