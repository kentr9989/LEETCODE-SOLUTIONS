class Solution:
    # Time complexity: O(log(m) + log(n))
    # Space complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top, bot = 0 , ROWS - 1
        
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top += 1
            elif matrix[mid][0] > target:
                bot -= 1
            else:
                break
        print(f"top: {top}")
        print(f"bot: {bot}")
        if top > bot:
            print(f"top: {top}")
            return False
        row = (top + bot) // 2
        left, right = 0 , COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left += 1
            elif matrix[row][mid] > target:
                right -= 1
            else:
                return True
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ROWS = len(matrix)
#         COLS = len(matrix[0])
        
#         top, bot = 0 , ROWS - 1
#         while top <= bot:
#             mid = (top + bot) // 2
#             if matrix[mid][-1] < target:
#                 top = mid + 1
#             elif matrix[mid][0] > target:
#                 bot = mid - 1
#             else:
#                 break
#         if top > bot:
#             return False
        
#         row = (top + bot) // 2
#         left , right = 0, COLS - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             if matrix[row][mid] < target:
#                 left = mid + 1
#             elif matrix[row][mid] > target:
#                 right = mid - 1
#             else:
#                 return True
#         return False
    
    
    
