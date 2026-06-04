class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        position_tracker = [True] * len(nums) # can use this spot

        def permute(subset):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if position_tracker[i] == False:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and position_tracker[i - 1] == False:
                    continue
                position_tracker[i] = False
                subset.append(nums[i])
                permute(subset)
                subset.pop()
                position_tracker[i] = True
            return result
        
        return permute([])
        