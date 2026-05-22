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
            return 
        node_to_clone = {}
        curr = head
        
        while curr:
            if curr in node_to_clone:
                curr = curr.next
            cloned = Node(curr.val)
            node_to_clone[curr] = cloned
            curr = curr.next
        
        new_curr = head
        while new_curr:
            if new_curr and new_curr.next:
                node_to_clone[new_curr].next = node_to_clone[new_curr.next]
            if new_curr and new_curr.random:
                node_to_clone[new_curr].random = node_to_clone[new_curr.random]
            new_curr = new_curr.next
        
        return node_to_clone[head]

            

        
        

            
            
            
            
            
            
            
