class Cashier:
    '''Требовалось реализовать класс в котором мы состаем объект кассира, который выдает скидки
    каждому N-ному посетителю и выдаёт чеки на оплату. Размер скидки передается вторым параметром
    Кроме того, есть список продуктов и цены на эти продукты. Списки одинаковы по длине.'''

    def __init__(self, n: int, discount: int, products: list, prices: list):
        self.n = n
        self.count = 0
        self.discount = (100 - discount) / 100
        self.prices = {products[i]: prices[i] for i in range(len(prices))}

    def getBill(self, product: list, amount: list) -> float:
        self.count += 1
        price = sum([self.prices[product[i]] * amount[i] for i in range(len(product))])
        if self.count % self.n == 0:
            return price * self.discount
        return price
