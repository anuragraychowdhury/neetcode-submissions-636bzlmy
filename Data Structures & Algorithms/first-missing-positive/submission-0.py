class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if correct_index < 0 or correct_index >= len(nums) or nums[i] == nums[correct_index]:
                i += 1
            elif 0 <= correct_index < len(nums) and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
        return len(nums) + 1