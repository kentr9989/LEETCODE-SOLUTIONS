class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        
        heapq.heapify(stones)
        # print(stones)
        # print(stones[-1])
        # print(stones[-2])
        # print(min_heap)
        # two_largest = heapq.nlargest(2,stones)
        # print(two_largest)
        while len(stones) > 1:
            two_largest = heapq.nlargest(2,stones)
            diff = two_largest[0] - two_largest[1]
            stones.remove(two_largest[0])
            stones.remove(two_largest[1])
            heapq.heapify(stones)
            heapq.heappush(stones,diff)
            
            
        
        
        return stones[0]
        
        
        # [1,1,2,4,7,8]
        # [1,1,1,2,4]