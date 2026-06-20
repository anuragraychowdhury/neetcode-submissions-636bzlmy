# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        left_ptr = dummy

        for i in range(left - 1):
            left_ptr = left_ptr.next
        previous_group_tail = left_ptr
        right_ptr = left_ptr

        for i in range(right - left + 1):
            right_ptr = right_ptr.next
        
        next_group_head = right_ptr.next
        
        chunk_start = left_ptr.next
        chunk_end = next_group_head

        prev = None
        curr = chunk_start
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        previous_group_tail.next = prev
        chunk_start.next = next_group_head

        return dummy.next

        
        
