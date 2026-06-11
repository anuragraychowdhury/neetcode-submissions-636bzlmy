class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        subset = []
        nums.sort()
        def permute():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                elif i > 0 and used[i - 1] == False and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                used[i] = True
                permute()
                subset.pop()
                used[i] = False
        permute()
        return res
        
                
        