class KthLargest:
    # Time complexity: O(n) - init heap * O(log (n - k)) - need to pop
    # Space complexity: O(n)
    def __init__(self, k: int, nums: List[int]):
        self.min_heap , self.max = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.max:
            heapq.heappop(self.min_heap)
        print(self.min_heap)
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.max:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)