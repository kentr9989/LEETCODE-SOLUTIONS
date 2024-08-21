# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity : O(n) not balanced and O(logn) balanced 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both tree empty:
        #   return True
        if not p and not q:
            return True
        # if one of the tree is empty:
        #   return False
        if not p or not q:
            return False
        
        # if value of p not equal value of q:
        #   return False
        if p.val != q.val:
            return False
        
        # return ( call recursive on p.left and q.left AND
        # call recursive on p.right and q.right)
        return (self.isSameTree(p.left, q.left) and
               self.isSameTree(p.right,q.right))
        
        
        