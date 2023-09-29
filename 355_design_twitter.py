class Twitter:
    '''
    lvl - Medium и я удивлен что мой runTime на 97 процентов лучше остальных решений.
    Требовалось реализовать класс, походий на ленту твиттов. Есть пара базовых методов. post - юзер с userID постит новый твит
    follow - первый юзер подписывается на второго юзера. unfollow - первый юзер отписывается от второго юзера.
    getNewsFeed - юзер с ID должен увидеть список твитов в порядке их размещения (от самого свежего к самому старому)
    в зависимости от того, на кого он сейчас подписан. Свои посты он тоже видит. Количество записей ограничено десятью единицами.
    '''
    def __init__(self):
        self.twitList = []
        self.followDict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitList.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> list:
        filterList = []
        finalList = []
        if userId in self.followDict:
            filterList.extend(self.followDict[userId])
        filterList.append(userId)

        for twits in self.twitList:
            if twits[0] in filterList:
                finalList.append(twits[1])

        finalList.reverse()
        return finalList[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDict:
            self.followDict[followerId] = []
        self.followDict[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followDict:
            lst = self.followDict[followerId]
            self.followDict[followerId].pop(lst.index(followeeId))


