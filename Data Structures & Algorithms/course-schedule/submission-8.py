class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for p in adjList[node]:
                status = dfs(p)
                if status == False:
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
        