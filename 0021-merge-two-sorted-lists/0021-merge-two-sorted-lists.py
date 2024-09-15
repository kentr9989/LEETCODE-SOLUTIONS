# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(l1 + l2)
    # Space complexity: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
    
#         # initially it look like this
#         # [dummy]/[tail]
#         # then later on
#         # [dummy] -> 1->2-> 3
#         #                   ^ (where tail is)
#         # so dummy->next will be [1]
        
#         # create dummy node
#         dummy = ListNode()
#         # init tail as dummy
#         tail = dummy
#         # while l1 and l2 is not null:
#         #   if current value of l1 < current value of l2:
#         #       tail.next = l1
#         #       l1 = l1.next
#         #   else:
#         #       tail.next = l2
#         #       l2 = l2.next
#         #   tail equal tail.next
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else: 
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#         # find non empty list
#         # if l1 not null:
#         #   tail.next = l1
#         # else if l2 not null: 
#         #   tail.next = l2
#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2
            
#         # return dummy.next
#         return dummy.next
        
        