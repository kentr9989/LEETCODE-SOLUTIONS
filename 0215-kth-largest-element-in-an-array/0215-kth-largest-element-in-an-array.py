class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        copy_heap = [-s for s in nums]
        heapify(copy_heap)
        res = 0
        while k > 0:
            val = -heapq.heappop(copy_heap)
            res = val
            k -= 1
        print(f"copy_heap: {copy_heap}")
        return res