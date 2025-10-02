class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)
        self.tweets = defaultdict()
        self.uid = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.uid += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.uid

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.user_follows[userId]
        users = set(follows)
        users.add(userId)
        tweets = [self.user_tweets[user][::-1][:10] for user in users]
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key=lambda tweet : self.tweets[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follows = self.user_follows[followerId]
        if followeeId in follows:
            follows.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
