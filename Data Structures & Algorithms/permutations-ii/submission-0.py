class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == True:
                    continue
                
                subset.append(nums[i])
                used[i] = True
                dfs(subset)
                subset.pop()
                used[i] = False
            return
        
        dfs([])
        return res
