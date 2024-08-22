# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # init n = 0
        # init stack = []
        # init curr = root
        n = 0
        stack = []
        curr = root
        # while curr and stack are not null:
        #   Keep traverse left as much as we can
        #   while curr is not null:
        #       append curr to the stack
        #       traverse left on curr
        #   pop from stack
        #   increase n by 1
        #   if n == k:
        #       return current value of val
        #   move curr to right
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        
        