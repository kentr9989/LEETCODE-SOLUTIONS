# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # if not root
        #   return 0
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        ##################################################################
        # Interative BFS
        # if root is null return 0
        if not root:
            return 0
        # init level 0
        level = 0
        # init queue with only root
        q = deque([root])
        # while q is not null:
        #   loop from i to length of q:
        #       pop left from queue
        #       if node.left not null:
        #           append node.left to queue
        #       if node.irhgt not null:
        #           append node.right to queue
        #   increase level by 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        # return level
        return level
        ####################################################################
        
        # Iterative DFS preorder
        # if root is null return 0
        # init stack when [root,depth of 1]
        # init res = 1
        # while stack is not null is not null:
        #   pop the node and depth from stack
        #   if node not null:
        #       res = max(res,depth)
        #       add children of node (left and right) with new depth to stack
        
        # return res
        
        