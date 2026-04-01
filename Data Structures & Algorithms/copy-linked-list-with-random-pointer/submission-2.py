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
        
        node_to_clone = {}
        curr = head
        
        while curr:
            node_to_clone[curr] = Node(curr.val)
            curr = curr.next
        
        temp = head
        while temp:
            cloned = node_to_clone[temp]
            if temp.next:
                cloned.next = node_to_clone[temp.next]
            if temp.random:
                cloned.random = node_to_clone[temp.random]
            temp = temp.next
        
        return node_to_clone[head]


            

        
        

            
            
            
            
            
            
            
