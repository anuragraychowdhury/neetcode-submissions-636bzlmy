class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)

            if a_parent == b_parent:
                return False
            
            if rank[a_parent] >= rank[b_parent]:
                rank[a_parent] += rank[b_parent]
                parent[b_parent] = a_parent
            else:
                rank[b_parent] += rank[a_parent]
                parent[a_parent] = b_parent
            
            return True
        
        components = n
        for a,b in edges:
            if union(a,b):
                components -= 1
        
        return components