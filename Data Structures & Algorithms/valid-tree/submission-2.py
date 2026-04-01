class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
