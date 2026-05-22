"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
create node_to_clone dict and then iterate through the cloned version of the list 
and start doing the rewiring as we see it
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # step 1: link clones to original node
        curr = head
        while curr:
            cloned = Node(curr.val)
            cloned.next = curr.next
            curr.next = cloned
            curr = cloned.next
        
        # step 2: link cloned nodes to their random clones
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # step 3: link a dummy head to the new list that is just deep copies
        dummy = Node(0, head)
        curr = head
        deep_copy_curr = dummy
        while curr:
            deep_copy_curr.next = curr.next
            deep_copy_curr = deep_copy_curr.next

            curr.next = curr.next.next
            curr = curr.next
        
        return dummy.next

