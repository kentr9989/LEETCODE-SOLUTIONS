# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time complexity: O(root * subRoot)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is empty : return true
        if not subRoot:
            return True
        # if root is not empty : return false
        if not root:
            return False
        # check with sameTree function
        # if it is:
        #   return true
        if self.sameTree(root,subRoot):
            return True
        # Return (call recursive isSubtree of (s.left,t) OR 
        # call recursive isSubtree of (s.right,t))
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def sameTree(self,s,t):
        # if s is empty and t is empty:
        #   return True
        if not s and not t:
            return True
        # if s is not empty and t is not empty and val of s = val of t
        #   return call recurse (s.left,t.left) and (s.right,t.right)
        if s and t and s.val == t.val:
            return self.sameTree(s.left,t.left) and self.sameTree(s.right, t.right)
        # return false
        return False