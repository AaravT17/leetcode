import heapq


class Twitter:
    def __init__(self):
        self.user_data = {}  # maps user -> tweets, followed users
        self.time = 0  # used as a timestamp for tweets, incremented each time a new tweet is posted

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_data:
            self._init_user_data(userId)
        self.user_data[userId]['tweets'].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.user_data:
            return []

        max_heap = []
        user_tweets = self.user_data[userId]['tweets']
        if user_tweets:
            max_heap.append((-user_tweets[-1][1], user_tweets, len(user_tweets) - 1))

        followed_users = self.user_data[userId]['followed_users']
        for user in followed_users:
            if user not in self.user_data:
                continue
            user_tweets = self.user_data[user]['tweets']
            if user_tweets:
                max_heap.append((-user_tweets[-1][1], user_tweets, len(user_tweets) - 1))

        heapq.heapify(max_heap)

        res = []
        while max_heap and len(res) < 10:
            timestamp, user_tweets, idx = heapq.heappop(max_heap)
            res.append(user_tweets[idx][0])
            if idx > 0:
                idx -= 1
                heapq.heappush(max_heap, (-user_tweets[idx][1], user_tweets, idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.user_data:
            self._init_user_data(followerId)
        self.user_data[followerId]['followed_users'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_data:
            return
        self.user_data[followerId]['followed_users'].discard(followeeId)

    def _init_user_data(self, user_id: int) -> None:
        self.user_data[user_id] = {'tweets': [], 'followed_users': set()}


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
