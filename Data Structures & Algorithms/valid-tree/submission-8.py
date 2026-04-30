class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(node, parent):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)

            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node) == False:
                    return False
            
            visiting.remove(node)
            visited.add(node)

            return True
        
        return dfs(0,None) and len(visited) == n

                
            