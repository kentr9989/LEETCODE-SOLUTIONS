# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left,right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
#         # create dummy node to head
#         dummy = ListNode(0,head)
#         # init left pointer to dummy
#         left = dummy
#         # init right pointer to head + n (use loop)
#         right = head
#         while n > 0 and right:
#             right = right.next
#             n -= 1
#         # while right is not null:
#         #   shift left = left.next
#         #   right = right.next
#         while right:
#             left = left.next
#             right = right.next
            
#         # delete the node
#         # left.next = left.next.next
#         left.next = left.next.next
        
#         # return dummy.next
#         return dummy.next