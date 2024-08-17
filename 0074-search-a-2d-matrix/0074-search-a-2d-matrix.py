class Solution:
    # Time complexity: O(log(m) + log(n))
    # Space complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ROWS = len of matrix
        ROWS = len(matrix)
        # COLS = len of matrix[0]
        COLS = len(matrix[0])
                
        # init top = 0
        top = 0
        # init bottom ROWS -1
        bot = ROWS - 1
        
        # while top <= bottom:
        #   middle = (top + bot) // 2
        #   if target greater than matrix[middle][-1] - greatest value in the row:
        #       top = middle + 1
        #   else if targer < matrix[row][0] - smallest value in the row:
        #       bottom = middle - 1
        #   else:
        #       break
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else: 
                break
        
        # if top > bottom:
        #    return False
        if top > bot:
            return False
        
        # row = (top + bottom) // 2
        # l,r = 0 , COL -1
        # while left <= right:
        #   mid = (left + right) // 2
        #   if (target > matrix[row][mid]):
        #       left = mid + 1
        #   else if targer < matrix[row][mid]:
        #       right = mid + 1
        #   else:
        #       return True
        row = (top + bot) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        
        # return False
        return False