class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        # init res 
        res = 0
        # init left pointer 0
        # init right pointer as length of height - 1
        left = 0
        right = len(height) - 1
        
        # while left is less than right:
        #   area equal (right - left) * min(height[left],height[right])
        #   update res to be max of res or area
        #   if height of left < height of right:
        #       increment left pointer
        #   else if height of left > height of right:
        #       decrement right pointer
        #   else:
        #       increment either one
        
        while left < right:
            area = (right - left) * min(height[left],height[right])
            res = max(area,res)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else: 
                right -= 1
        
        #   return max res
        return res
        