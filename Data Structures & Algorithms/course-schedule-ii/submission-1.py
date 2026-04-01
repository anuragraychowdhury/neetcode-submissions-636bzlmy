class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)
        
        visited = set()
        visiting = set()
        path = []

        def dfs(course):
            if course in visiting:
                return []
            if course in visited:
                return True
            
            visiting.add(course)
            for nxt in adjList[course]:
                if dfs(nxt) == []:
                    return []
            
            visiting.remove(course)
            visited.add(course)
            path.append(course)

            return True
        
        for c in range(numCourses):
            if dfs(c) == []:
                return []
        
        return path