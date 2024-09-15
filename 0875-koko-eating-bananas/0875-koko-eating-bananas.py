class Solution:
    # Time complexity: O(log(max(piles)*piles))
    # Space complexity: O(max(piles))
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
        
        
        
#         # left is equal 1 (bc need to eat least 1 banana)
#         left = 1
#         # right is equal max(piles) - last index
#         right = max(piles) # piles[-1]
#         # res = right
#         res = right
#         # while left is less than or qual right:
#         #   mid = left + right / 2
#         #   hours = 0
#         #   go to every pile:
#         #       hours += math.ceil(pile/mid)
        
#         #   if hours (mid) <= h (target):
#         #       update res
#         #       right = mid - 1 (search left portion)
#         #   else:
#         #       left = mid + 1 (search for right portion)
#         while left <= right:
#             mid = (left + right) // 2
#             hours = 0
#             for pile in piles:
#                 hours += math.ceil(pile/mid)
            
#             if hours <= h:
#                 res = min(mid,res)
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         # return res
#         return res