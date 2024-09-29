class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair of index , height
        
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea, (i - index) * height )
                start = index
            stack.append([start,h])
        print(maxArea)
        while stack:
            curr_index, curr_height = stack.pop()
            maxArea = max(maxArea, (len(heights) - curr_index) * curr_height)
        return maxArea