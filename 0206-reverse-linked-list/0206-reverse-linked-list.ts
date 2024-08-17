/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseList(head: ListNode | null): ListNode | null {
        // Iterative solution
        // [A]<-[B]<-[C]
        // Init prev as NULL
        let prev: ListNode | null = null;
        // Init curr as head
        let curr: ListNode | null = head;

        // while curr is not NULL:
            // store temp node => ([B])
            // curr->next = prev  =>  (NULL<-[A])
            // prev = curr => (prev = [A])
            // curr = temp node => ([B])
        while (curr !== null) {
            let temp: ListNode | null = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }  

        // return prev
        return prev;
       
    
};