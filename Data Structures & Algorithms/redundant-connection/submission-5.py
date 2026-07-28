class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(node):
            while node != parent[node]:
                node = find(parent[node])
            return node
        
        def union(nodeA, nodeB):
            parentA = find(nodeA)
            parentB = find(nodeB)

            if parentA == parentB:
                return False
            
            if rank[parentA] >= rank[parentB]:
                parent[parentB] = parentA
                rank[parentA] += rank[parentB]
            else:
                parent[parentA] = parentB
                rank[parentB] += rank[parentA]
            
            return True
        
        for a,b in edges:
            if union(a,b) == False:
                return [a,b]
        