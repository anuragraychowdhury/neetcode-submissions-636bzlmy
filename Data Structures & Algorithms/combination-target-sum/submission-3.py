class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, subset, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum > target or index == len(nums):
                return
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(i, subset, curr_sum + nums[i])
                subset.pop()

        dfs(0,[],0)
        return res





            