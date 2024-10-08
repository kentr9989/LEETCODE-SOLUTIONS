# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive sol
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Base case: If head is null or head->next is null:
        #   return head
        # Recursively the rest of the list and assign to new head
        # head->next->next = head
        # head->next = null
        # return new head
#         if not head or not head.next:
#             return head
        
#         newHead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
        
#         return newHead
        
        # # Iterative sol
        # Time complexity: O(n)
        # Space complexity: O(1)
            prev = None
            curr = head
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
            
            
            
            
            
            
            
            
            
       
#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev
        