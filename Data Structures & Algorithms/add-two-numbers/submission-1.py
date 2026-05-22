# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2 or carry_over:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
            
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
            
            total = l1_val + l2_val + carry_over
            carry_over = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next