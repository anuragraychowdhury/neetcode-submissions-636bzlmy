class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(start_index, subset):
            res.append(subset.copy())

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
            return 
        
        dfs(0, [])
        return res