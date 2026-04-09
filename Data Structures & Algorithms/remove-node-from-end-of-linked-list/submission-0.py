# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        i = dummy

        counter = 0
        while counter != n:
            i = i.next
            counter += 1
        
        curr = dummy
        while i.next:
            i = i.next
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next