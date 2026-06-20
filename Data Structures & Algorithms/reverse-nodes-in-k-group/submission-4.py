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
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        chunk_start = head
        dummy = ListNode(0, head)
        previous_group_tail = dummy

        while True:
            chunk_end = chunk_start
            for i in range(k):
                if chunk_end == None:
                    break
                chunk_end = chunk_end.next
            # we finished the loop successfully, we can perform a reverse
            else:
                new_head = reverse(chunk_start, chunk_end)
                previous_group_tail.next = new_head
                previous_group_tail = chunk_start
                chunk_start = chunk_end
                continue
            # we did not finish the loop successfully, so we need to connect the previous group tail with our chunk start and break out
            previous_group_tail.next = chunk_start
            previous_group_tail = chunk_start
            chunk_start = chunk_end
            break
        
        return dummy.next
        

            

