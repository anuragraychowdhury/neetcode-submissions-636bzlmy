# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            fast  = fast.next.next
            slow = slow.next
        
        # slow is one spot behind the second half of the node
        # first half is stored by dummy.next

        head_second_half = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        while head_second_half:
            next_node = head_second_half.next
            head_second_half.next = prev
            prev = head_second_half
            head_second_half = next_node
        
        # merge the lists
        head_one = dummy.next
        head_two = prev

        while head_one and head_two:
            nxt_head_one = head_one.next
            nxt_head_two = head_two.next

            head_one.next = head_two
            head_two.next = nxt_head_one

            head_one = nxt_head_one
            head_two = nxt_head_two




            
