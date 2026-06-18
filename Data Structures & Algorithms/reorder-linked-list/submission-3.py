# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the linked list down the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split the lists
        second_head = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        curr = second_head
        while curr:
            nxt_node = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_node
        
        # interleave the lists
        curr_one = head
        curr_two = prev
        while curr_one and curr_two:
            next_node_one = curr_one.next
            next_node_two = curr_two.next
            
            curr_one.next = curr_two
            curr_two.next = next_node_one

            curr_one = next_node_one
            curr_two = next_node_two

            




