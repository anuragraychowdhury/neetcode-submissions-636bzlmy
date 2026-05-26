# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(float('inf'), head)
        left_ptr = dummy
        left_cnt = 0
        right_ptr = dummy
        right_cnt = 0

        while left_cnt != left - 1:
            left_ptr = left_ptr.next
            left_cnt += 1
        first_half = left_ptr.next
        
        while right_cnt != right:
            right_ptr = right_ptr.next
            right_cnt += 1

        prev = None
        curr = left_ptr.next
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        
        left_ptr.next = prev
        first_half.next = curr

        return dummy.next