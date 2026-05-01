class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a,b):
            parent_a = find(a)
            parent_b = find(b)

            if rank[parent_a] >= rank[parent_b]:
                parent[parent_b] = parent_a
                rank[parent_a] += rank[parent_b]
            else:
                parent[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]
            
            return
        
        for a,b in edges:
            if find(a) == find(b):
                return [a,b]
            else:
                union(a,b)


