class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        copy_stone = [-s for s in stones]
        heapq.heapify(copy_stone)
        print(copy_stone)
        while len(copy_stone) > 1:
            first,second = -heapq.heappop(copy_stone), -heapq.heappop(copy_stone)
            print(f"first: {first}")
            print(f"second: {second}")
            if first > second:
                diff = (first - second) * (-1) 
                heapq.heappush(copy_stone,diff)
            print(copy_stone)
        print(copy_stone)
        return abs(copy_stone[0]) if len(copy_stone) > 0 else 0;
        
        
        # [4,2]
        # 2
        
        
        
        
        
        
        
#         Time complexity: O(n^2)
#         Space complexity: O(1)
#         if len(stones) == 1: return stones[0]
        
#         heapq.heapify(stones)
#         while len(stones) > 1:
#             two_largest = heapq.nlargest(2,stones)
#             diff = two_largest[0] - two_largest[1]
#             stones.remove(two_largest[0])
#             stones.remove(two_largest[1])
#             heapq.heapify(stones)
#             heapq.heappush(stones,diff)
            
            
        
        
#         return stones[0]
        
        
        # [1,1,2,4,7,8]
        # [1,1,1,2,4]