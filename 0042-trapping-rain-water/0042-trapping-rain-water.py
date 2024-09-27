class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def trap(self, height: List[int]) -> int:
        left,right = 0 , len(height) - 1
        res = 0
        max_left, max_right = height[left], height[right]
        
        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left,height[left])
                if max_left - height[left] < 0:
                    res = res + 0
                else: 
                    res += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right,height[right])
                if max_right - height[right] < 0:
                    res = res + 0
                else: 
                    res += max_right - height[right]
                right -= 1
        return res
                