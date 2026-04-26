class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for prereq, course in prerequisites:
            adjList[course].append(prereq)
        
        prereqs = {}
        def dfs(node):
            if node in prereqs:
                return prereqs[node]
            
            curr_set = set()
            for prereq in adjList[node]:
                curr_set.add(prereq)
                curr_set |= dfs(prereq)
            
            prereqs[node] = curr_set
            return curr_set
        
        for course in range(numCourses):
            dfs(course)
        
        res = []
        for u,v in queries:
            if u in prereqs[v]:
                res.append(True)
            else:
                res.append(False)
        return res

        

                


