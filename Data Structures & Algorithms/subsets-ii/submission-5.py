class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(start_index, subset):
            if start_index == len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[start_index])
            dfs(start_index + 1, subset)
            subset.pop()

            while start_index + 1 < len(nums) and nums[start_index + 1] == nums[start_index]:
                start_index += 1
            
            dfs(start_index + 1, subset)
            
            return
        
        dfs(0, [])
        return res