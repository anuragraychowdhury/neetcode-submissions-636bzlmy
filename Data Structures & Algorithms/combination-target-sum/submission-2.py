class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, subset, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            if curr_sum > target or index == len(nums):
                return
            
            curr_sum += nums[index]
            subset.append(nums[index])
            dfs(index, subset, curr_sum)
            popped = subset.pop()
            curr_sum -= popped

            dfs(index + 1, subset, curr_sum)

        dfs(0,[],0)
        return res





            