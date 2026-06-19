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
        
        group_start = head
        dummy = ListNode(0, head)
        prev_group_tail = dummy

        while True:
            group_end = group_start
            for i in range(k):
                if group_end == None:
                    break
                group_end = group_end.next
            else:
                new_tail = group_start
                new_head = reverse(group_start, group_end)
                prev_group_tail.next = new_head
                prev_group_tail = new_tail
                group_start = group_end
                continue
            
            prev_group_tail.next = group_start
            break
        return dummy.next
                











