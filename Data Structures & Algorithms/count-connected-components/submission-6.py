class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a,b):
            parent_a = find(a)
            parent_b = find(b)

            if parent_a == parent_b:
                return
            
            if rank[parent_a] >= rank[parent_b]:
                parent[parent_b] = parent_a
                rank[parent_a] += rank[parent_b]
            else:
                parent[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]
            
            return
        
        for n1,n2 in edges:
            union(n1,n2)
        
        res = set()
        for p in parent:
            curr = find(p)
            if curr in res:
                continue
            res.add(curr)
        return len(res)



            
