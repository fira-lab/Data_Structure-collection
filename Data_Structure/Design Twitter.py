from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.tweets[userId])

        for follower in self.followers[userId]:
            tweets.extend(self.tweets[follower])

        tweets.sort(key=lambda x: x[0], reverse=True)

        return [tweet[1] for tweet in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)