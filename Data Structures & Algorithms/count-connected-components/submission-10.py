class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node != parent[node]:
                node = find(parent[node])
            return node
        
        def union(nodeA, nodeB):
            parent_A = find(nodeA)
            parent_B = find(nodeB)

            if parent_A == parent_B:
                return 
            
            elif rank[parent_A] >= rank[parent_B]:
                parent[parent_B] = parent_A
                rank[parent_A] += rank[parent_B]
            else:
                parent[parent_A] = parent_B
                rank[parent_B] += rank[parent_A]
            return 
        
        for a,b in edges:
            union(a,b)
        
        return len(set(find(i) for i in range(n)))
        
        
