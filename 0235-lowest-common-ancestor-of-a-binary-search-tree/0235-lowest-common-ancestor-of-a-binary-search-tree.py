# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # start at root node assign to cur
        curr = root
        # while curr is not null:
        #   if value of p > value of cur and value of q > value of cur:
        #       cur = cur.right
        #   else if value of p < value of cur and value of p < value of cur:
        #       cur = cur.left
        #   else:
        #       return cur
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        
        