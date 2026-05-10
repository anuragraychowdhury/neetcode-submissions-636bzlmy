class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i]
            if correct_index < len(nums) and nums[correct_index] != nums[i]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums) 