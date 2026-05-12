# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reversal(head, end_node):
            if not head:
                return None
            c = head
            p = end_node
            while c != end_node:
                nxt = c.next
                c.next = p
                p = c
                c = nxt
            return p
        
        dummy = ListNode(None, head)
        curr = dummy
        k_ptr = dummy
        count = 0

        while k_ptr.next != None:
            count = 0
            k_ptr = curr
            while count != k:
                if k_ptr.next == None:
                    return dummy.next
                k_ptr = k_ptr.next
                count += 1
            tail = curr.next
            next_head = k_ptr.next
            new_head = reversal(curr.next, next_head)
            curr.next = new_head
            tail.next = next_head
            curr = tail
        return dummy.next 