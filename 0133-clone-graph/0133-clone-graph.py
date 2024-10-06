"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(curr):
            if not curr: 
                return None
            if curr in oldToNew:
                return oldToNew[curr]
            
            copy = Node(curr.val)
            oldToNew[curr] = copy
            
            # add neighbour
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
                
        return dfs(node)