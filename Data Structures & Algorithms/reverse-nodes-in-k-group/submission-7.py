# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(left, right):
            curr = left
            prev = None
            while curr != right:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        start = head
        end = head

        while True:
            for i in range(k):
                if not end:
                    break
                end = end.next
            else:
                # enter the else if we have succesfully finished the for loop - there is a group
                new_head = reverse(start, end)
                prev_group_tail.next = new_head
                prev_group_tail = start
                start = end
                continue
            
            prev_group_tail.next = start
            break
        
        return dummy.next
        
        









