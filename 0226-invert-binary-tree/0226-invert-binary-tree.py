# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is null 
        #   return null
        if not root:
            return None
        # swap the children
        # save temp to root.left
        # root.left = root.right
        # root.right = temp
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # recursive invert left subtree
        self.invertTree(root.left)
        # recursive invert right subtree
        self.invertTree(root.right)
        
        # return the root
        return root