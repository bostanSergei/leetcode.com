class UndergroundSystem:
    '''Требуется описать структуру, которая будет учитывать пользователей, которые зашли и вышли из подземки,
    при этом счиать время, которое пассажиры потратили для перемещения между станцией А и Б, отдавая по запросу
    среднее время, за которое можно добраться от одной точки до второй'''
    def __init__(self):
        self.timeDict = {}
        self.inList = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inList.append([id, stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        index = -1
        for i in range(len(self.inList)):
            if self.inList[i][0] == id:
                index = i
                break
        currientPassenger = self.inList.pop(index)
        station = tuple([currientPassenger[1], stationName])
        if station not in self.timeDict:
            self.timeDict[station] = [t - currientPassenger[2]]
        else:
            self.timeDict[station].append(t - currientPassenger[2])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timeList = self.timeDict[tuple([startStation, endStation])]
        return sum(timeList) / len(timeList)


