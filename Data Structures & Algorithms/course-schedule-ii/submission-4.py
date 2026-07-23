class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = set()
        visiting = set()
        path = []

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for neighbor in adjList[node]:
                if dfs(neighbor) == False:
                    return False
            visiting.remove(node)
            visited.add(node)
            path.append(node)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return path 

