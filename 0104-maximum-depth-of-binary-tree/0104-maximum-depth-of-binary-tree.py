# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS:
        # Time complexity O(n)
        # Space complexity O(logn)
        # if not root: 
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ##################################################################
        # Interative BFS
        # Time complexity O(n)
        # Space complexity O(n)
#         if not root: 
#             return 0
        
#         level = 0
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
#         return level
        ####################################################################
        
        # Iterative DFS preorder
        if not root: 
            return 0
        stack = [[root,1]]
        res = 0
        
        while stack:
            node, level = stack.pop()
            # print(f"node: {node}")
            # print(f"level: {level}")
            if node.left:
                stack.append([node.left,level + 1])
            # print(f"node: {node}")
            # print(f"level: {level}")
            if node.right:
                stack.append([node.right,level + 1])
            res = max(res,level)
        return res
        
        
        
        
        
        
        
        
        
        # if root is null return 0
#         if not root:
#             return 0
#         # init stack when [root,depth of 1]
#         stack = [[root,1]]
#         # init res = 1
#         res = 1
#         # while stack is not null is not null:
#         #   pop the node and depth from stack
#         #   if node not null:
#         #       res = max(res,depth)
#         #       add children of node (left and right) with new depth to stack
#         while stack:
#             node,depth = stack.pop()
#             if node:
#                 res = max(res,depth)
#                 stack.append([node.left,depth + 1])
#                 stack.append([node.right,depth + 1])
                
#         # return res
#         return res
        