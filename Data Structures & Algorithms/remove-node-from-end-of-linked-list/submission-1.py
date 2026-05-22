# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy
        n_ptr = dummy
        count = 0

        while count != n:
            n_ptr = n_ptr.next
            count += 1
        
        while n_ptr.next:
            curr = curr.next
            n_ptr = n_ptr.next
        
        curr.next = curr.next.next
        return dummy.next