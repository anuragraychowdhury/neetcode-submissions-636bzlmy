class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        visiting = set()

        def dfs(node, parent_node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent_node:
                    continue
                if dfs(neighbor, node) == False:
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        res = dfs(0, None)
        if res == False:
            return False
        elif res == True and len(visited) != n:
            return False
        else:
            return True
            


