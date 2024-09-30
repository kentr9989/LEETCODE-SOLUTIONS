# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time complexity: O(n)
        # Space complexity : O(1)
        
        # find the middle point
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start_of_second = slow.next
        slow.next = None # cut the link btwn first and second
        
        prev = None
        
        # reverse second link list
        second = start_of_second
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head,prev
        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = tmp1
            first.next = second
            first = tmp1
            second = tmp2
       
            
        

        
        
        
        
        
        
        
        
#         # Find the middle
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         # print(slow)
#         # print(fast)
#         # Reverse the second half
#         second = slow.next
#         prev = None
#         # break the half link
#         slow.next = None
#         while second:
#             temp = second.next
#             second.next = prev
#             prev = second
#             second = temp
#         print(prev)
#         # Merge the two list
#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next , second.next
#             first.next = second
#             second.next = tmp1
#             second = tmp2
#             first = tmp1
    
        