# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def valid(curr, low ,high) :
            if not curr:
                return True
            
            if not (curr.val > low and curr.val < high) :
              return False
            
            return valid(curr.left,low,curr.val) and valid(curr.right,curr.val,high)
        
        return valid(root,float("-infinity"), float("infinity"))
        
        # (2, -inf , inf)
        # valid(1,-inf,2)  -> True           and valid(3,2,inf)
        # valid(null, -inf, 1) and val(null,1,inf) -> True
        #    True and True
    #     2
    #    / \
    #   2    2      
    #  / \  / \
    # n   n 3  6
        
        
        
        
        
#         # create function to traverse dfs
#         def valid(node, low , high):
#             # if node is null:
#             #   return true
#             if not node:
#                 return True
#             # if value is not between low and high:
#             #   return false
#             if not (low < node.val < high):
#                 return False
#             # return (node.left, low, node.val) AND
#             #        (node.right, node.val, high)               
#             return (valid(node.left,low,node.val) and
#                    valid(node.right,node.val,high))
            
#         # return call the valid
#         return valid(root,float("-inf"),float("inf"))
        