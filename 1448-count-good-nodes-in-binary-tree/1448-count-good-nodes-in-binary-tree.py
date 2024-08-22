# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Create a function to traverse dfs
        def dfs(node,maxVal):
            # if node is null:
            #   return 0
            if not node:
                return 0
            
            # if value of node is greater than or equal to maxVal:
            #   res = 1
            # else:
            #   res is 0
            res = 1 if node.val >= maxVal else 0
            
            # update maxVal between maxVal and value of node
            maxVal = max(maxVal,node.val)
            # res += recurse dfs of the left side
            # res += recurse dfs on the right side
            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)
            
            # return res
            return res
        # call dfs on the rood node
        return dfs(root,root.val)
    