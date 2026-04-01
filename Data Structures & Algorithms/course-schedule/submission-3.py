class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for crs, prereq in prerequisites:
            adjList[prereq].append(crs)
        
        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nxt in adjList[course]:
                if dfs(nxt) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True

