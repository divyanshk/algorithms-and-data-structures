# Problem: https://leetcode.com/problems/design-twitter/description/
import heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userMap = {}
        self.followMap = {}
        self.counter = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.userMap:
            self.userMap[userId] = []
        self.userMap[userId].append((-self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        userFeedHeap = set([])
        if userId in self.userMap:
            userFeedHeap.update(self.userMap[userId])
        if userId in self.followMap:
            for followee in self.followMap[userId]:
                if followee in self.userMap and followee is not userId:
                    for tweet in self.userMap[followee]:
                        userFeedHeap.add(tweet)

        heapq.heapify(list(userFeedHeap))
        return [] if not userFeedHeap else map(lambda x:x[1], heapq.nsmallest(10, userFeedHeap))
                
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followMap:
            self.followMap[followerId] = set([])
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
