class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(start_index, subset):
            res.append(subset.copy())

            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
            return
            
        
        dfs(0,[])
        return res