class KthLargest:
    '''Требуется реализовать класс в котором при создании экземпляра подаётся два элемента: порядковый номер k
    и список стартовых чисел. Каждый раз при вызове метода add требуется добавить новое число в список, отсортировать
    его и вернуть k-ый (по величине (то есть с конца)) элемент последовательности'''
    def __init__(self, k: int, nums: list):
        self.k, self.nums = k, nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]