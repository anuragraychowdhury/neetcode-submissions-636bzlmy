class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hashset = defaultdict(set)
        adjList = defaultdict(set) # course : prereq
        for a,b in prerequisites:
            adjList[b].add(a)

        def dfs(node):
            if node in hashset:
                return hashset[node] # return a set
            
            for prereq in adjList[node]:
                p_set = dfs(prereq)
                hashset[node].update(p_set)
                hashset[node].add(prereq)
            
            return hashset[node]
        
        # set up prereq dict
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u,v in queries:
            if u in hashset[v]:
                res.append(True)
            else:
                res.append(False)
        return res


            

        