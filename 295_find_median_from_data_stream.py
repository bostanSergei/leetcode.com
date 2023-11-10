class MedianFinder:
    '''
    Идея задачи в следующем: нам один за другим подаются числа. В указанной последовательности нам переодически
    требуется возвращать медиану нашей последовательности. В решении я чет прям наворотил... Но все ограничения
    были пройдены, что очень даже не плохо, учитывая lvl задачи - hard
    Итак, смысл в том, чтобы каджый раз при получении нового значения запускать алгоритм бинарного поиска для
    понимания того, куда именно мы будем вставлять то самое новое значение. Алгоритм получился с костылями, но
    всё работает, а это уже хорошо)
    '''
    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        left, right = 0, len(self.lst) - 1

        if len(self.lst) == 0:
            self.lst.append(num)
            return None
        if num <= self.lst[0]:
            self.lst.insert(0, num)
            return None
        if num >= self.lst[-1]:
            self.lst.append(num)
            return None
        if abs(right - left) == 1 and self.lst[left] < num < self.lst[right]:
            self.lst.insert(right, num)
            return None

        middle = (left + right) // 2
        while abs(left - right) > 1:
            middle = (left + right) // 2
            if self.lst[middle] == num:
                self.lst.insert(middle, num)
                return None

            elif abs(right - left) == 1 and self.lst[left] < num < self.lst[right]:
                self.lst.insert(right, num)
                return None

            elif self.lst[middle] < num:
                left = middle

            else:
                right = middle

        if abs(right - left) == 1 and self.lst[left] < num < self.lst[right]:
            self.lst.insert(right, num)
            return None

        self.lst.insert(middle, num)

    def findMedian(self) -> float:
        if len(self.lst) % 2 == 1:
            return float(self.lst[len(self.lst) // 2])

        index = len(self.lst) // 2
        return (self.lst[index] + self.lst[index - 1]) / 2
