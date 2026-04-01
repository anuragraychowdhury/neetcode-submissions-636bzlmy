# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_iter = l1
        l2_iter = l2
        carry_on = 0

        dummy = ListNode(-1)
        curr = dummy

        while l1_iter or l2_iter or carry_on:
            x = l1_iter.val if l1_iter else 0
            y = l2_iter.val if l2_iter else 0
            total = x + y + carry_on
            
            node_val = total % 10
            carry_on = total // 10
            
            new_node = ListNode(node_val)
            curr.next = new_node
            curr = curr.next
            
            if l1_iter:
                l1_iter = l1_iter.next
            if l2_iter:
                l2_iter = l2_iter.next
        
        return dummy.next
                

            