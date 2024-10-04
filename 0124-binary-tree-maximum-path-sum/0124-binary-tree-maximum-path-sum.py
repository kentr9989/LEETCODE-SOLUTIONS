# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(curr):
            if not curr:
                return 0
            
            # print(curr.val)
            
            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)
            leftMax = max(0,leftMax)
            rightMax = max(0,rightMax)
            
            
            # With split
            res[0] = max(res[0], curr.val + leftMax + rightMax)
            print(f"self.res[0]: {res[0]}")
            
            # Return without split
            return curr.val + max(leftMax,rightMax)
        
        dfs(root)
        
        return res[0]
    
        # res = 6
        # dfs(1) (leftMax = 2, rightMax = 3 )
        # leftMax = dfs(2) (leftMax = 0 , rightMax = 0)
        #   leftMax = dfs(n) => 0
        #   rightMax = dfs(n) => 0
        # rightMax = dfs(3) (leftMax = 0 , rightMax = 0)
        
        
        
        
        
        
        
            
            
            
            