"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_to_clone = {}
        def clone_graph(node):
            if node in node_to_clone:
                return node_to_clone[node]
            
            cloned = Node(node.val)
            node_to_clone[node] = cloned
            for neighbor in node.neighbors:
                cloned_neigbor = clone_graph(neighbor)
                node_to_clone[node].neighbors.append(cloned_neigbor)
            
            return cloned
        
        return clone_graph(node)
        
        
        
