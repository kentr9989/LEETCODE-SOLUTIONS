class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            curr_area = (r - l) * min(height[r],height[l])
            max_area = max(curr_area,max_area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else: 
                r -= 1
        return max_area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        

        