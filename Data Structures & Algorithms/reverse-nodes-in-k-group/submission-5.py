# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(left, right):
            prev = None
            curr = left
            while curr != right:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        dummy = ListNode(-1, head)
        previous_group_tail = dummy
        chunk_start = head

        while True:
            chunk_end = chunk_start
            for i in range(k):
                if chunk_end == None:
                    break
                chunk_end = chunk_end.next
            else:
                new_head = reverse(chunk_start, chunk_end)
                previous_group_tail.next = new_head
                previous_group_tail = chunk_start
                chunk_start = chunk_end
                continue

            previous_group_tail.next = chunk_start
            chunk_start = chunk_end
            break
        return dummy.next





