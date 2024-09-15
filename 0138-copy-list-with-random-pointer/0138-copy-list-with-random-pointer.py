"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        old_to_copy = {}
        
        curr = head
        # 1st pass
        while curr:
            copy_curr = Node(curr.val)
            old_to_copy[curr] = copy_curr
            curr = curr.next
       
        # 2nd pass
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy.get(curr.next)
            copy.random = old_to_copy.get(curr.random)
            curr = curr.next
        return old_to_copy[head]
#         # Init old_to_copy hashMap {old_node: copy}
#         old_to_copy = {None : None}
        
#         # Init current to be the head
#         curr = head
        
#         # 1st pass to copy old -> copy to the hashmap
#         while curr:
#             copy_curr = Node(curr.val)
#             old_to_copy[curr] = copy_curr
#             curr = curr.next
            
#         # 2nd pass to assign random and next to copy
#         curr = head
#         while curr:
#             copy = old_to_copy[curr]
#             copy.next = old_to_copy[curr.next]
#             copy.random = old_to_copy[curr.random]
#             curr = curr.next
#         # return the head of copy from hashMap
#         return old_to_copy[head]