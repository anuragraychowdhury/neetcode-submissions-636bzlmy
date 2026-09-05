class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visiting = set()
        visited = set()

        def dfs(node, parent_node):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent_node:
                    continue
                cycle_check = dfs(neighbor, node)
                if cycle_check == True:
                    return True
            
            visiting.remove(node)
            visited.add(node)

            return False
        
        cycle_present = dfs(0, None) 
        if cycle_present:
            return False
        elif not cycle_present and len(visited) != n:
            return False
        else:
            return True


            
            