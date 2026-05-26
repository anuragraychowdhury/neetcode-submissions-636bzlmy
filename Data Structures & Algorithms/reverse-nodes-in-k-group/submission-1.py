# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(start, end):
            prev = None
            curr = start
            for i in range(k):
                nxt_node = curr.next
                curr.next = prev
                prev = curr
                curr = nxt_node
            return prev
        
        dummy = ListNode(float('inf'), head)
        start_ptr = dummy
        end_ptr = dummy
        end_cnt = 0

        while end_ptr:
            while end_cnt != k:
                end_ptr = end_ptr.next
                end_cnt += 1
                if end_ptr == None:
                    return dummy.next
                
            first_part_start = start_ptr
            tail = start_ptr.next
            next_part_start = end_ptr.next

            new_head = reverse(start_ptr.next, end_ptr)
            first_part_start.next = new_head
            tail.next = next_part_start

            start_ptr = tail
            end_ptr = tail
            end_cnt = 0
        
        return dummy.next





            




            