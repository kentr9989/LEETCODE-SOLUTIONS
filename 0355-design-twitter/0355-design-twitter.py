class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = {} # userId -> [count,tweetId]
        self.followMap = {} # userId -> (set of followeeId)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1 # for max-heap operation
        print(f"tweetMap: {self.tweetMap}")


    def getNewsFeed(self, userId: int) -> List[int]:
        print("get new feed")
        res = []
        minHeap = []
        
        # follow themself
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        print(f"followMap line 25: {self.followMap}")
        
        # Push min heap 
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # push the latest tweet
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count,tweetId,followeeId,index - 1]) #index-1 because of next index to track
        print(f"minHeap line 34: {minHeap}")
        
        # Heapify mean heap based on negative count (max heap)
        heapq.heapify(minHeap)
        print(f"minHeap line 38: {minHeap}")
        
        # retrieve the latest post from minHeap
        while minHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # reinsert the latest post of followeeId to minHeap
            if index >= 0:
                count,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId, index - 1])
            
            
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)
        print(f"followMap: {self.followMap}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)
        print(f"unFollowMap: {self.followMap}")


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)