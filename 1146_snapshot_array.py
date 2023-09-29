class SnapshotArray:
    '''Я хз как, но мое решение в medium lvl опять лучше чем 98% по run time. Сложно на русском объяснить что тут просходит
    и в чем суть задачи - лучше почитать про нее в оригинале. Бился долго и упорно. Решение в лоб залетело в memory limit,
    следующие решения уходили в ошибки на разных тестах, хотя по факту я сам в какой-то момент времени затупил и неверно
    отдавал значения по ключу. В итоге нашел свою ошибку на старте и пролетел на хорошей скорости) Радуюсь за себя)))'''

    def __init__(self, length: int):
        self.snapDict = {}
        self.shot = 0

    def set(self, index: int, val: int) -> None:
        if index not in self.snapDict:
            self.snapDict[index] = {}
            if self.shot > 0:
                self.snapDict[index] = {0: 0}
        self.snapDict[index][self.shot] = val

    def snap(self) -> int:
        self.shot += 1
        return self.shot - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snapDict:
            return 0
        else:
            if snap_id not in self.snapDict[index]:
                resList = self.snapDict[index].keys()
                resList = [key for key in resList]
                resList.append(snap_id)
                resList.sort()
                ind = resList.index(snap_id) - 1

                return self.snapDict[index][resList[ind]]

            return self.snapDict[index][snap_id]

