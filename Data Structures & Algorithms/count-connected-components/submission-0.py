class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        visited = set()

        scc = 0

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbors in adjList[node]:
                if node == prev:
                    continue
                if neighbors not in visited:
                    dfs(neighbors, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                scc += 1
        return scc





