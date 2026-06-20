# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        for i in range(left - 1):
            curr = curr.next
        
        prev_group_tail = curr
        left_node = curr.next

        right_node = left_node
        for i in range(right - left + 1):
            right_node = right_node.next
        next_group_head = right_node
        
        prev = None
        rev_curr = left_node
        new_tail = left_node

        for i in range(right - left + 1):
            next_node = rev_curr.next
            rev_curr.next = prev
            prev = rev_curr
            rev_curr = next_node
        
        prev_group_tail.next = prev
        new_tail.next = next_group_head

        return dummy.next
        

