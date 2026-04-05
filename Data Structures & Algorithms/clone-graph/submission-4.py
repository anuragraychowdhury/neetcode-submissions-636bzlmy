"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_to_clone = {}
        
        def dfs(node):
            if node in node_to_clone:
                return node_to_clone[node]
            if node == None:
                return
            clone = Node(node.val)
            node_to_clone[node] = clone

            for neighbor in node.neighbors:
                cloned = dfs(neighbor)
                node_to_clone[node].neighbors.append(cloned)
            
            return node_to_clone[node]
        
        return dfs(node)