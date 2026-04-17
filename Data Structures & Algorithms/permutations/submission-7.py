class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [True] * len(nums)

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i] == False:
                    continue
                subset.append(nums[i])
                used[i] = False
                dfs(subset)
                subset.pop()
                used[i] = True
            return
        
        dfs([])
        return res