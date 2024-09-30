class Solution:
    # Time Complexity: O(n * log M) where n is the number of piles, and M is the maximum pile size.
    # Space Complexity: O(1) (constant space).
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                res = mid
                right = mid - 1 
            else:
                left = mid + 1
        return res
        
        
        
        
        
        
        
        
        
#         left = 1
#         right = max(piles)
#         res = right
        
#         while left <= right:
#             mid = (left + right) // 2
#             hours = 0
#             for pile in piles:
#                 hours += math.ceil(pile/mid)
#             if hours <= h:
#                 res = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         return res
        
