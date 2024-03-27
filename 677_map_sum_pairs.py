class MapSum:
    def __init__(self):
        self.dct = {}

    def insert(self, key: str, val: int) -> None:
        self.dct[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, value in self.dct.items():
            if key.startswith(prefix):
                res += value

        return res
