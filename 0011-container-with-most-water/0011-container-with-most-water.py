class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1
        max_water = -1
        while left < right:
            curr_height = min(height[left],height[right])
            curr_width = right - left
            curr_water = curr_height * curr_width
            print(f"current water: {curr_water}")
            max_water = max(max_water,curr_water)
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return max_water
        
#         res = 0  
#         left, right = 0, len(height) - 1
#         while left < right:
#             area = (right - left) * min(height[left],height[right])
#             res = max(res,area)
#             if height[left] < height[right]:
#                 left += 1
#             elif height[left] > height[right]:
#                 right -= 1
#             else:
#                 right -= 1
                
#         return res  
        
#         # init res 
#         res = 0
#         # init left pointer 0
#         # init right pointer as length of height - 1
#         left = 0
#         right = len(height) - 1
        
#         # while left is less than right:
#         #   area equal (right - left) * min(height[left],height[right])
#         #   update res to be max of res or area
#         #   if height of left < height of right:
#         #       increment left pointer
#         #   else if height of left > height of right:
#         #       decrement right pointer
#         #   else:
#         #       increment either one
        
#         while left < right:
#             area = (right - left) * min(height[left],height[right])
#             res = max(area,res)
#             if height[left] < height[right]:
#                 left += 1
#             elif height[left] > height[right]:
#                 right -= 1
#             else: 
#                 right -= 1
        
#         #   return max res
#         return res
        