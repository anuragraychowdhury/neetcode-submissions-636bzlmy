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

        dummy = ListNode(0, head)      # lets us treat "group 1" the same as every other group
        prev_group_tail = dummy        # tracks the tail of whatever we've reversed so far
        group_start = head

        while True:
            group_end = group_start
            for i in range(k):
                if group_end is None:   # ran out of nodes before finding k of them
                    break
                group_end = group_end.next
            else:
                # for-loop completed all k iterations without breaking -> full group available
                new_tail = group_start                      # old head becomes the tail post-reversal
                new_head = reverse(group_start, group_end)   # reverse just this chunk
                prev_group_tail.next = new_head              # connect previous chunk's tail to this new head
                prev_group_tail = new_tail                    # this chunk's old head is now the tail
                group_start = group_end                       # advance to the next chunk
                continue                                      # go reverse the next group

            # only reached if the for-loop broke -> not enough nodes left, leave as-is
            prev_group_tail.next = group_start
            break

        return dummy.next
            











