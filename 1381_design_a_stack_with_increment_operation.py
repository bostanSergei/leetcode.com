class CustomStack:

    def __init__(self, maxSize: int):
        self.stack, self.maxSize = [], maxSize

    def push(self, x: int) -> None:
        if len(self.stack) + 1 <= self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            num = self.stack.pop()
            return num
        return -1

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)
        for i in range(k):
            self.stack[i] += val

