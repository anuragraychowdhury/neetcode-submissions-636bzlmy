class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start_index, subset):
            res.append(subset.copy())  # add at every level
            
            for i in range(start_index, len(nums)):
                subset.append(nums[i])     # choose
                dfs(i + 1, subset)        # explore forward
                subset.pop()              # backtrack
        
        dfs(0, [])
        return res