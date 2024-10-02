# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(logn)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diammeter = 0
        
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.diammeter = max(self.diammeter, left + right)
            return 1 + max(left,right)
            
        
        
        
        dfs(root)
        return self.diammeter
        
        
        
        
        
        
        
        
        
        
        
        
#         self.res = 0 # global variable
        
        
#         # Return the height
#         def dfs(curr):
#             if not curr:
#                 return 0
#             left = dfs(curr.left)
#             right = dfs(curr.right)
#             self.res = max(self.res, left + right)
#             return max(left,right) + 1
#         dfs(root)
#         return self.res
            