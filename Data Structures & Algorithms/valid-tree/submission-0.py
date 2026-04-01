class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        
        visit = set()
        adjList = defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for edges in adjList[node]:
                if edges == prev:
                    continue
                if dfs(edges, node) == False:
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        

        return len(visit) == n
                

        