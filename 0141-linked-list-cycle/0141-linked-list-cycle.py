# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            while slow == fast:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
#         if not head:
#             return False
#         slow, fast = head, head.next
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
            
#         return False
        
        