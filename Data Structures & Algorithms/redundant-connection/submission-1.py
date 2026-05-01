class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        
        def dfs(source, target, visited):
            if source == target:
                return True

            visited.add(source)
            for neighbor in adjlist[source]:
                if neighbor in visited:
                    continue
                if dfs(neighbor, target, visited) == True:
                    return True
            return False
        

        for a,b in edges:
            visited = set()
            verdict = dfs(a,b,visited)
            if verdict == True:
                return [a,b]
            else:
                adjlist[a].append(b)
                adjlist[b].append(a)
                    