# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reversed_curr = slow.next
        slow.next = None
        prev = None
        
        while reversed_curr:
            nxt_node = reversed_curr.next
            reversed_curr.next = prev
            prev = reversed_curr
            reversed_curr = nxt_node
        
        new_curr = prev

        while curr and new_curr:
            nxt_curr = curr.next
            nxt_new_curr = new_curr.next

            curr.next = new_curr
            new_curr.next = nxt_curr
            
            curr = nxt_curr
            new_curr = nxt_new_curr
            

        
