class MedianFinder:

    def __init__(self):
        # self.small maxheap
        # self.large minheap
        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        # push num to small heap
        heapq.heappush(self.small,num * -1) #-1 to make a max heap
        
        # check if largest of small is greater than min of large
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            largest_of_small = heapq.heappop(self.small) * -1
            heapq.heappush(self.large,largest_of_small)
        # check if len of small is greater than large + 1
        if len(self.small) > len(self.large) + 1:
            largest_of_small = heapq.heappop(self.small) * -1
            heapq.heappush(self.large,largest_of_small)
        if len(self.large) > len(self.small) + 1:
            smallest_of_large = heapq.heappop(self.large)
            heapq.heappush(self.small, smallest_of_large * -1)
        # print(f"small: {self.small}")
        # print(f"large: {self.large}")
        
           

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        # print(f"small: {self.small}")
        # print(f"large: {self.large}")
        return (-1 * self.small[0] + self.large[0]) / 2
        
# [1] [2]        
        

# [4,2]   [3]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()