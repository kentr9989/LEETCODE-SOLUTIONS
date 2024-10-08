# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        res = []
        q = deque([root])
        res.append(root.val)
        
        while q:
            temp_arr = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    temp_arr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    temp_arr.append(node.right.val)
            res.append(temp_arr[-1]) if len(temp_arr) > 0 else None
        
        return res
                
        
        
        
#         # Init res = []
#         res = []
#         # Init queue with root
#         queue = deque([root])
        
#         # while queue is not null:
#         #   init rightSideNode
#         #   loop from i = 0 to length of queue:
#         #       pop the left from queue
#         #       if node is not null:
#         #           assign the value to rightSideNode
#         #       append the pop left node to stack
#         #       append the pop right node to stack
#         #   if rightSideNode is not null
#         #       append it to the res
#         while queue:
#             rightSideNode = None
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node:
#                     rightSideNode = node
#                     queue.append(node.left)
#                     queue.append(node.right)
#             if rightSideNode:
#                 res.append(rightSideNode.val)
#         # return res
#         return res