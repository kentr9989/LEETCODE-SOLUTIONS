# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative sol
        # [A]<-[B]<-[C]
        # Init prev as NULL
        prev = None
        # Init curr as head
        curr = head
        # while curr is not NULL:
        #   store temp node => ([B])
        #   curr->next = prev  =>  (NULL<-[A])
        #   prev = curr => (prev = [A])
        #   curr = temp node => ([B])
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # return prev
        return prev