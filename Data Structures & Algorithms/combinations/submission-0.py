class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(start_index, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            
            for i in range(start_index, n + 1):
                subset.append(i)
                dfs(i + 1, subset)
                subset.pop()
            
        dfs(1,[])
        return res

                