class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for a,b in prerequisites:
            adjList[a].append(b)
        
        visiting = set()
        visited = set()
        path = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for neighbor in adjList[node]:
                if dfs(neighbor) == False:
                    return False
    
            visiting.remove(node)
            path.append(node)
            visited.add(node)

            return True
        
        for c in range(numCourses):
            if c in visited:
                continue
            elif dfs(c) == False:
                return []
        return path