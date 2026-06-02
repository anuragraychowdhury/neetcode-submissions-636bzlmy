class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            current_number = nums[i]
            if 1 <= current_number < len(nums):
                if nums[i] != nums[current_number - 1]:
                    nums[current_number - 1], nums[i] = nums[i], nums[current_number - 1]
                else:
                    i += 1
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1  