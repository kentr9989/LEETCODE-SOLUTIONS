# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) queue at any given point have up to n/2 elements
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        res.append([root.val])
        while q:
            temp_arr = []
            for i in range(len(q)):
                node = q.popleft()
                # print(f"node: {node}")
                if node.left:
                    q.append(node.left)
                    temp_arr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    temp_arr.append(node.right.val)
            res.append(temp_arr) if len(temp_arr) > 0 else None
            # print(res)
        return res   
        
        
        
        
        
        
        
        
#         # if root is empty return []
#         if not root:
#             return []
#         # init queue first element of [root]
#         queue = collections.deque()
#         queue.append(root)
        
#         # create res with []
#         res = []
#         # while queue is not empty:
#         #   create res1 to be []
#         #   for i in range (0 to len(q)):
#         #       node = pop left element
#         #       if node 
#         #           add to res1
#         #           append node.left to queue
#         #           append node.right to queue
#         #               append to queue
#         #       if res1 is not empty:
#         #           add res1 to res
#         while queue:
#             res1 = []
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node:
#                     res1.append(node.val)
#                 if node.left:
#                     queue.append(node.left)  # append left child to queue
#                 if node.right:
#                     queue.append(node.right)  # append right child to queue
#             if res1:
#                 res.append(res1)
                    
        
#         #  return res
#         return res