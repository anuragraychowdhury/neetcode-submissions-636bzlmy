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

        dummy = ListNode(-1, head)
        group_start = head
        group_end = head
        prev_group_tail = dummy

        while True:
            for i in range(k):
                if group_end == None:
                    break
                group_end = group_end.next
            # for else; else triggers when for loop completes
            else:
                new_head = reverse(group_start, group_end)
                prev_group_tail.next= new_head
                prev_group_tail = group_start
                group_start = group_end
                continue
            
            # if we are outside the else, that means the for loop didn't finish
            # that means that there aren't enough nodes
            prev_group_tail.next = group_start
            group_start = group_end
            break
        
        return dummy.next
        





            




        