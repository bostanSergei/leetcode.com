from collections import deque


class RecentCounter:

    def __init__(self):
        self.lst = deque()

    def ping(self, t: int) -> int:
        self.lst.append(t)

        while t - self.lst[0] > 3000:
            self.lst.popleft()

        return len(self.lst)
