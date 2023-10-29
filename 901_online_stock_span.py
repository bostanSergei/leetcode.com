class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        result = 1
        while self.data and self.data[-1][0] <= price:
            result += self.data.pop()[1]

        self.data.append((price, result))
        return result
